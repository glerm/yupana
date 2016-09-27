#encoding: utf-8
# autor: rafael polo
require 'rubygems'
require 'rdf'
require 'rdf/raptor'

class ConsultaNatural

  @ns = "http://www.baixogavea.com/rdf/album"
  @graph = RDF::Graph.load("repositorio.rdf")

  def self.pergunta?(frase)
    return frase.length>0 && frase[-1].chr == "?"
  end

  def self.interpreta(pergunta)
    consulta = {}
    if self.pergunta?(pergunta)
      pergunta.gsub!(",", "")
      remover = ["qual", "quais", "os", "as", "a", "o", "que", "da", "do", "de", "e"]
      remover.each  do |str|
        regex = Regexp.new("\\b#{str}\\b", Regexp::IGNORECASE)
        pergunta.gsub!(regex, "")
      end
      break_line
      # pega tokens compostos
      tokens_compostos = pergunta.scan(/"([\w\s]+)"/)
      # retira compostos
      pergunta.gsub!(/"[\w\s]+"/, "")
      # tokens
      tokens_simples = pergunta.chop.split(" ")
      tokens = tokens_simples + tokens_compostos
      # para cada token
      tokens.each do |token|
        if semlabel = self.semantic_label(token.to_s)
          consulta[semlabel.keys.to_s.intern] = semlabel.values if semlabel
        else
          puts "token: #{token}"
        end
      end
    else
      return false
    end
    return consulta
  end

  def self.responde(consulta)
    return ["Isso não é uma pergunta."] if !consulta

    sujeito = predicado = objeto = nil
    resposta = []

    # qual da tripla falta?
    sujeito = RDF::URI.new(consulta[:subject]) if consulta[:subject]
    predicado = RDF::URI.new(consulta[:predicate]) if consulta[:predicate]
    objeto = consulta[:object] if consulta[:object]

    query_fato = [sujeito, predicado, objeto]
    if query_fato.uniq.count==3
      query = @graph.query(query_fato)
      if query.count>0
        query.each do |fato|
          if sujeito==nil
            resposta << fato.subject
          end
          if predicado==nil
            resposta << "Sim." if !fato.predicate.to_s.empty?
          end
          if objeto==nil
            resposta << fato.object.to_s
          end
        end
        return resposta
      else
        return ["Não sei."]
      end
    else
      puts query_fato
      return ["Não entendi."]
    end
  end

  # classe, propriedade, valor
  def self.semantic_label(token)
    #sujeito | album
    uri_token = RDF::URI.new(token)
    if @graph.has_subject?(uri_token)
      # quantos = fatos / predicados de sua classe
      quantos =  (@graph.query([uri_token, nil, nil]).count / @graph.predicates.count)
      # os sujeitos do repositório são álbuns
      puts "sujeito: Album = #{token} (#{quantos})"
      return {:subject=>uri_token}
    end

    #predicado
    if token.index(" ")==nil #namespace não pode ter espaço
      uri_token = RDF::URI.new(@ns+'#'+token)
      if @graph.has_predicate?(uri_token)
        # sinonimos ?
        puts "predicado: Album.#{token}" if @graph.has_predicate?(token.intern)
        return {:predicate=>uri_token}
      end
    end

    #objeto
    if @graph.has_object?(token)
      # todos os predicados/atributos com esse token/valor são os mesmos?
      atributos = []
      @graph.query([nil, nil, token]).each do |fato|
        atributos << fato.predicate
      end
      if atributos.uniq.count==1
        attr = atributos[0].to_s.gsub(@ns+"#", "")
        puts "objeto: Album.#{attr} = #{token} (#{ @graph.query([nil, nil, token]).count})"
      end
      return {:object=>token}
    end

  end

end

def break_line
  puts "="*50
end