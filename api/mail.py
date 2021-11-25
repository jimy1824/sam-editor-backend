from django.template.loader import render_to_string
from django.template import Template, Context
from django.utils.encoding import force_text


def send_register_email(user, data):
    # try:
        subject, from_email, to = 'Invoice', settings.EMAIL_HOST_USER, [user.email]
        html = render_to_string('email_templates.html',
                                data
                                )
        content = Template(html).render(Context({}))
        msg = EmailMultiAlternatives(subject, content, from_email, to)
        msg.attach_alternative(content, "text/html")
        msg.send()
    # except Exception as e:
    #     pass
