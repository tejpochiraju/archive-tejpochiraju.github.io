---
layout: post
title:  "Decoupling authentication and identity"
date:   2021-01-30
categories: privacy
published: true
---

![Login Fields](/assets/images/login_fields.png)

What do you most commonly enter in that username field? Your email, your phone number?

Hold that thought. We will return to it.

In a [previous post](/supporting-newspapers-harms-privacy.html) I explored why my privacy is more at risk when _paying_ for a newspaper than when not. My proposals, however, were `mostly wrong`.

---

## Of logical fallacies

Specifically, I proposed the creation of a payment processor who would double as an identity provider (IDP). As [@jackerhack pointed out](https://twitter.com/jackerhack/status/1354977856154075138), this puts too much power in the hands of the payment processor.

In [reply](https://twitter.com/tejpochiraju/status/1355024191859290113), I proposed a flow that seemingly solves the privacy issues with the newspaper and the payment processor. Except, I got there through `flawed logic`.

To summarize:

- User clicks on subscribe
- Newspaper sends user to a payment processor
- User completes payment and is granted a random, generated token.
- The same token is given to the newspaper which stores it as proof of subscription.
- User is granted access anytime they present that token.

That bit about the generated token aside, the rest of the flow is exactly what already happens. So, the privacy "gains" result purely from using a random token to login instead of a username/password combination.

---

## Back to the top

So, that username field - what's your most common id? 

Mine's an old email address. It's lasted me well over ten years - a constant companion while I switched countries and phone numbers. And oh, to make it easy for folks to remember, it's just my_first_name.my_last_name@gmail.com. 

Given the dominance of GMail, I imagine this is true for most of us. So, there's an `easily guessable` email ID that is the thread linking all of my services together.

Besides, it's not far fetched to say that this email address has been my defacto online **identity**.

## What is authentication and why is it using my identity?

We all accept that services need to authenticate us before they will grant access. Most of us have password managers with hundreds of websites, perhaps 10s of passwords, a couple of email IDs and may be one phone number.

So, essentially, the act of logging into a service as me (or you) consists mostly of guessing my password. Which is to say that the username/password form may as well be just a password form. 

Of course, this is not without flaws.

- There's _some_ entropy from having two fields to guess instead of one. 
- Many of us have the same passwords so the username is essential to tell us apart.

## There's a better model v2. This time with a maybe.

My challenge, and perhaps yours, is that we make profiling far too easy by using the same identity across services. Given the context of centralised apps, I see a few potential solutions. 

### Containerised Identities

In this scenario, we create separate identities for each service we sign up for. Kind of like `first_name+netflix@gmail.com` except perhaps a bit more clever. 

I recently switched to using [Tutanota](https://tutanota.com/) with a custom domain as my email service. So any _x@tejpochiraju.in_ is a valid email ID. With some simple filters, I catch subscriptions, bills and randoms in different folders. 

I could then use _netflix@tejpochiraju.in_, _dropbox@tejpochiraju.in_ and so on to keep my identities siloed. That is until some clever sod figures out the domain name part of it. 

The domain name is also the primary problem with scaling my approach - how many folks have and set up their own email domains?

Alternatively, how about asking our browsers to generate a unique login id along with the password for each sign up? This would work - if we didn't ever need that password reset link sent to a working email.

### Unique Passwords For All

Typically, authentication systems enforce uniqueness on the username. We could enforce it on the password instead. This makes the username field redundant. 

This does not have to be a race where the first person to use `password123` gets to use it. There are simple existing methods that could work.

The most popular of these is the Universally unique identifier [`UUID`](https://en.wikipedia.org/wiki/Universally_unique_identifier). This is a 36 character string that looks like this: **123e4567-e89b-12d3-a456-426614174000**.

> While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible. - [Wiki Pedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)

Assuming we are all using password managers (and we should be), remembering this sequence is a job we leave to tools.

But most apps don't need 36 character passwords to ensure uniqueness. Blokada uses 12 character codes. With lowercase/ uppercase letters and digits, this allows `62^12 = 3226266762397899821056` unique codes. Should suffice for a long while yet!

### Cryptographic Keys

[Assymetric cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) using public/private key pairs has been used to secure protocols such as ssh, MQTT and even Bitcoin. This post is already too long to go into details here but suffice to say that:

- You could generate a unique key for each service
- Give the public key to the service to store
- Each time you want to access the service, engage in a complex handshake that proves you are the owner of the private key
- Gain access

This is perhaps the most secure and private authentication system we know. Admittedly, this is a more complex paradigm shift. Our browsers and web services are not built for this mode of authentication. But, perhaps, the day is not too far where we may need them to be.

## Where do we go from here?

For the moment, I have made the following choices:

- Where an email or phone number is not mandatory, I don't give one. Even if this means I can't receive password reset emails.
- Where an email is necessary, I use _servicename@tejpochiraju.in_
- I am trying to minimise services that require my phone number.
- I secure my passwords using a password manager **and** a secure backup, just in case.

I am still finding my feet with these topics so if you have insights and reads for me please do share at _privacy@tejpochiraju.in_.

