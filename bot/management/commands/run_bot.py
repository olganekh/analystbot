from django.core.management.base import BaseCommand
from bot.handling_bot.core import run_bot


class Command(BaseCommand):
    help = 'Запускать пулинг телеграм бота'

    def handle(self, *args, **options):
        print('Бот запущен')
        run_bot()
