from django.db import models
from django.contrib.auth.models import User

class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)

class Service(models.Model):
    CHOISES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Реврайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография')

    ]

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    service_type = models.CharField(choices=CHOISES, default='1', max_length=1)
    price = models.IntegerField()

    def __str__(self):
        return "{}, {}, price: {}".format(self.name. self.get_service_type_display(), self.price)

class Order(models.Model):
    CHOISES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Реврайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография')

    ]

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    service_type = models.CharField(choices=CHOISES, default='1', max_length=1)
    price = models.IntegerField()

    def __str__(self):
        return "{}, {}, price: {}".format(self.name. self.get_service_type_display(), self.price)

class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)

class Ordering(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return "{} - {}, Customer: {}, Executor: {}".format(self.order_date, self.deadline,
                                                            self.customer, self.executor)

class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    desc = models.CharField(max_length=1000)

class Ticket(models.Model):
    SEVERITIES = [
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Высокая')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    is_resolved = models.BooleanField(default=False)
    ticket_date = models.DateTimeField()
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return "{}, {}, is resolved? {}".format(self.get_severity.display(),
                                                self.ticket_date, self.is_resolved)
class Review(models.Model):
    RATING_FILLED = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]

    rating = models.CharField(choices=RATING_FILLED, default='1', max_length=1)
    desc = models.CharField(max_length=1000)

class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return "{}, {}".format(self.author, self.review_date)
