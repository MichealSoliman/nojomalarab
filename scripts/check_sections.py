import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see the reviews section
reviews = re.search(r'<section id="reviews"[\s\S]*?</section>', text)
if reviews:
    print('Reviews section found, length:', len(reviews.group(0)))

trust_details = re.search(r'<section id="trust-details"[\s\S]*?</section>', text)
if trust_details:
    print('Trust-details section found, length:', len(trust_details.group(0)))

contact = re.search(r'<section id="contact"[\s\S]*?</section>', text)
if contact:
    print('Contact section found, length:', len(contact.group(0)))

