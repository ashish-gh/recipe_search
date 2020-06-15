Hi there,

Someone asked for a password reset for the email address {{ email }}.
Follow the link below:
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

In case you forgot your Recipe Search username: {{ user.username }}

If clicking the link above doesn't work, please copy and paste the URL
in a new browser window instead.

If you've received this mail in error, it's likely that another user entered
your email address by mistake while trying to reset a password. If you didn't
initiate the request, you don't need to take any further action and can safely
disregard this email.

Thanks,

The Django Boards Team