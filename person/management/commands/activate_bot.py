import json
import random

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker
from progress.bar import Bar

from person.service import create_post, get_access_token, create_user, like_posts


class Command(BaseCommand):
    help = 'active bot to demonstrate functionality of API'
    default_value = 5

    def handle(self, *args, **options):
        config = json.load(open("bot_config.json"))
        number_of_users = config.get('number_of_users', self.default_value)
        max_posts = config.get('max_posts_per_user', self.default_value)
        max_likes = config.get('max_likes_per_user', self.default_value)
        bar = Bar('Create user with posts...', max=number_of_users)
        fake = Faker()

        post_id_list = []
        tokens = []

        for _ in range(number_of_users):
            credentials = {
                "username": fake.user_name(),
                "password": f"{fake.last_name()}{fake.first_name()}"
            }
            data = {
                **credentials,
                "email": fake.email() if fake.boolean(60) else ""
            }

            try:
                create_user(data)
            except (ValueError, IntegrityError):
                pass
            else:
                token = get_access_token(credentials)
                tokens.append(token)

                for _ in range(random.randint(1, max_posts)):
                    post_data = {
                        "title": fake.paragraph(),
                        "content": fake.text() if fake.boolean(40) else "",
                        "draft": fake.boolean(),
                    }
                    post_id_list.append(create_post(post_data, token))

            bar.next()
        bar.finish()

        print("Users and Post were created")
        like_bar = Bar("Post liking...", max=number_of_users)

        for token in tokens:
            post_for_like = [post_id for post_id in post_id_list if fake.boolean(60)]

            like_posts(token, post_for_like)

            like_bar.next()

        like_bar.finish()
