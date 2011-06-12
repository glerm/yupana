# -*- coding: utf-8 -*-

from mechanize import Browser
br = Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open( "http://lite.facebook.com/" )
br.select_form(nr=0)
br.form['email'] = 'yupanakernel@gmail.com'
br.form['password'] = 'yourpassword'
br.submit()
br.select_form(nr=1)
br.form['message'] = 'Quem me chamou?'
br.submit()


#Read more: http://bayu.freelancer.web.id/2009/11/20/automate-facebook-status-update-without-facebook-api/#ixzz1P4cvdyAk
#Under Creative Commons License: Attribution

