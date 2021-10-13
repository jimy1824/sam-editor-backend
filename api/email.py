from django.conf import settings
from django.template.loader import render_to_string
from django.template import Template, Context
from django.core.mail import EmailMultiAlternatives


def send_register_email(email, data):
    # try:
    subject, from_email, to = 'Order Confirmation', settings.EMAIL_HOST_USER, [email]
    html = render_to_string('email_templates.html',
                            {'data': data}
                            )
    content = Template(html).render(Context({}))
    msg = EmailMultiAlternatives(subject, content, from_email, to)
    msg.attach_alternative(content, "text/html")
    msg.send()
# except Exception as e:
#     pass
