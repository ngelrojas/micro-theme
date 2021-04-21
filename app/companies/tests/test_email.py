import json
from unittest.mock import patch
from django.test import TestCase, Client
from django.core import mail


# class EmailUnitTest(TestCase):
#     def test_send_email_should_succed(self) -> None:
#         with self.settings(
#             EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
#         ):
#             mail.send_mail(
#                 subject="subject mockup",
#                 message="message mockup",
#                 from_email="info@yopmail.com",
#                 recipient_list=["info@rednodes.com"],
#                 fail_silently=False,
#             )
#             self.assertEqual(len(mail.outbox), 1)
#             self.assertEqual(mail.outbox[0].subject, "subject mockup")

#     def test_send_email_empty(self) -> None:
#         """ the mocked have to be equal to view function"""
#         client = Client()
#         with patch("companies.views.send_mail") as mocked_send_mail_function:
#             response = client.post(path="/send-email")
#             response_content = json.loads(response.content)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response_content["status"], "success")
#             self.assertEqual(response_content["info"], "email sent successfully")
#             mocked_send_mail_function.assert_called_with(
#                 subject=None,
#                 message=None,
#                 from_email="info@yopmail.com",
#                 recipient_list=["info@rednodes.com"],
#             )

#     def test_send_email_with_verb_should_fail(self) -> None:
#         client = Client()
#         response = client.get(path="/send-email")
#         assert response.status_code == 405
#         assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}

# Native PYTEST
def test_send_email_should_success(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0
    mail.send_mail(
        subject="subject mockup",
        message="message mockup",
        from_email="info@yopmail.com",
        recipient_list=["info@rednodes.com"],
        fail_silently=False,
    )
    assert len(mail.outbox) == 1
    assert mailoutbox[0].subject == "subject mockup"


def test_send_email_empty(client) -> None:
    """ the mocked have to be equal to view function"""
    client = Client()
    with patch("companies.views.send_mail") as mocked_send_mail_function:
        response = client.post(path="/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"
        mocked_send_mail_function.assert_called_with(
            subject=None,
            message=None,
            from_email="info@yopmail.com",
            recipient_list=["info@rednodes.com"],
        )


def test_send_email_with_verb_should_fail(client) -> None:
    response = client.get(path="/send-email")
    assert response.status_code == 405
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
