import secrets


def generate_django_secret_key(length=50):
  allowed_chars=(
      'abcdefghijklmnopqrstuvwxyz'
      'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  )
  return ''.join(secrets.choice(allowed_chars) for i in range(length))


if __name__ == "__main__":
  print(generate_django_secret_key())
  