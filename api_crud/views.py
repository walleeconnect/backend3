# utils.py or views.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_model_instance_created_email(sender, instance, **kwargs):
    # Customize this function based on your email sending logic
    print('send_model_instance_created_email')
    try:
        # Load a template to render the email content
        #email_template = 'email_templates/model_instance_created_email.html'
        context = {'model_instance': instance}
        email_subject = f'New {sender.__name__} Created'

        # Render the email template with the provided context
        #email_body = render_to_string(email_template, context)

        # Strip HTML tags for the plain text version of the email
        email_body_plain = strip_tags(context)

        from_email = 'walleeconnect@gmail.com'
        recipient_list = ['walleeconnect@gmail.com']
        print('********')
        print(email_subject)
        print('********')
        print(instance)
        send_mail(
            email_subject,
            email_body_plain,
            from_email,
            recipient_list,
            html_message=""  # Include the HTML version of the email
        )
    except Exception as e:
        print(e)


