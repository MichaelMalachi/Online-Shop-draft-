# product/tests.py
from django.test import TestCase, override_settings
from django.urls import reverse
from django.core import mail
from .models import Products, CustomUser123
from .tasks import send_welcome_email

class ProductsModelTest(TestCase):

    def setUp(self):
        # Создаем тестовый продукт для использования в тестах
        self.product = Products.objects.create(
            name='Тестовый продукт',
            description='Тестовое описание',
            price=100
        )

    def test_create_product(self):
        # Тестирование создания продукта
        product = Products.objects.create(
            name='Новый продукт',
            description='Новое описание',
            price=200
        )
        self.assertEqual(product.name, 'Новый продукт')
        self.assertEqual(product.description, 'Новое описание')
        self.assertEqual(product.price, 200)

    def test_read_product(self):
        # Тестирование чтения продукта
        product = Products.objects.get(id=self.product.id)
        self.assertEqual(product.name, 'Тестовый продукт')
        self.assertEqual(product.description, 'Тестовое описание')
        self.assertEqual(product.price, 100)

    def test_update_product(self):
        # Тестирование обновления продукта
        self.product.name = 'Обновленное название'
        self.product.save()
        updated_product = Products.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, 'Обновленное название')

    def test_delete_product(self):
        # Тестирование удаления продукта
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(id=product_id)

# Новый тест для задачи отправки приветственного письма
class SendWelcomeEmailTaskTest(TestCase):

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_send_welcome_email_task(self):
        email = 'testuser@example.com'
        # Запускаем задачу
        send_welcome_email.delay(email)
        # Проверяем, что письмо было отправлено
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, 'Добро пожаловать на наш сайт!')
        self.assertIn('Спасибо за регистрацию.', sent_email.body)
        self.assertEqual(sent_email.from_email, 'no-reply@mysite.com')
        self.assertEqual(sent_email.to, [email])

# Тест для проверки отправки письма при регистрации пользователя
class UserRegistrationEmailTaskTest(TestCase):

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_registration_sends_email_task(self):
        # Проверяем, что перед тестом почтовый ящик пуст
        self.assertEqual(len(mail.outbox), 0)

        # Данные для регистрации
        registration_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123',
        }

        # Отправляем POST-запрос на регистрацию
        response = self.client.post(reverse('register'), registration_data)

        # Проверяем, что пользователь перенаправлен после регистрации
        self.assertRedirects(response, reverse('home'))

        # Проверяем, что было отправлено одно письмо
        self.assertEqual(len(mail.outbox), 1)

        # Проверяем содержание письма
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Добро пожаловать на наш сайт!')
        self.assertIn('Спасибо за регистрацию.', email.body)
        self.assertEqual(email.from_email, 'no-reply@mysite.com')
        self.assertEqual(email.to, ['testuser@example.com'])

        # Проверяем, что пользователь создан в базе данных
        user_exists = CustomUser123.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)
