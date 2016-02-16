#!/usr/bin/env python3

from cement.core.foundation import CementApp


class SmtpUtf(CementApp):

    class Meta:
        label = 'smtp_utf'
        extensions = ['ext.ext_smtp_utf']

    def send(self):
        self.mail.send(body='Текст', subject='Тема')

with SmtpUtf() as app:
    app.run()
    app.send()
