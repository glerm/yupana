puts "Carregando..."
require 'rubygems'
require 'xmpp4r/client'
require 'xmpp4r/roster'
include Jabber
puts "Carregando Repositório..."
require 'consulta_natural'

Jabber::debug = true

# conectar
puts "Conectando..."
client = Client.new(JID::new("agente@baixogavea.com/bot"))
client.connect
client.auth("agentebaixogavea*")
client.send(Presence.new(nil, "consulta-natural v0.2").set_type(:available))
roster = Roster::Helper.new(client)
puts "Conectado!"

# aceitar qualquer usuário como amigo
roster.add_subscription_request_callback do |item, pres|
  puts "Subscription de: #{pres.from}"
  roster.accept_subscription(pres.from)
  client.send(Message::new(pres.from, "Olá, bem-vindo à embarcação."))
  client.send(Message::new(pres.from, 'Todo meu conhecimento é construído coletivamente através do http://baixogavea.com, são 107 usuários, 2913 bandas e 6661 álbuns. Colabore!'))
  client.send(Message::new(pres.from, "Atualmente vc pode me perguntar sobre a relação entre bandas, albuns, seu ano, o usuario que o adicionou e onde fazer o download."))
  save_history(pres.from.to_s.split("/")[0], "Subscription")
end

# responder consultas
client.add_message_callback do |m|
  if m.body
    puts "Consulta: #{m.body}"
    save_history(m.from.to_s.split("/")[0], m.body)
    if consulta = ConsultaNatural.interpreta(m.body)
      respostas = ConsultaNatural.responde(consulta)
    else
      respostas = ["Isso não foi uma pergunta."]
    end
    respostas.each do |resposta|
      msg = Message::new(m.from, resposta.to_s)
      msg.type=:chat
      client.send(msg)
      save_history(m.from.to_s.split("/")[0], "> "+resposta)
    end
  end
end

def save_history(de, str)
  path = File.dirname(__FILE__)
  filename = "#{path}/history/#{de}.txt"
  quando = Time.now.strftime("%d-%m-%Y %I:%M:%S")
  txt = "#{quando}: #{str}\n"
  File.open(filename, 'a') {|f| f.write(txt) }
end

while true
  # mantém vivo
end
