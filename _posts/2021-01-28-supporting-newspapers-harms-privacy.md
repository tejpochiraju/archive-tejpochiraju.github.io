---
layout: post
title:  "Supporting newspapers harms your privacy"
date:   2021-01-28
categories: privacy
published: true
---

I am a Gaurdian reader. Have been since 2006. 

I am a Guardian subscriber. Have been, on & off, since they introduced subscriptions.

I still see this banner every time I go to the site. (OK, I would if I didn't have an adblocker.)

![Guardian Subscriber Plea](/assets/images/guardian_subscriber_plea.png)

---

> The point I am clumsily trying to make is that I pay but I don't sign in. 


When I don't sign in, I have the _option_/_notion_ of rejecting all tracking. **Once I sign in, all bets are off.**

![Guardian Privacy Settings](/assets/images/guardian_privacy_settings.png)

---

Thankfully, the Guardian only has annoying ads and not a paywall. Unlike the other newspapers I subscribe to.

| Newspaper I pay for   | Can I read without logging in?    |
| ---                   | ---                               |
| The Hindu             | No                                |
| The New York Times    | No                                |
| Wall Street Journal   | No                                |
| Live Mint             | Yes                               |
| The Guardian          | Yes                               |


## Why do newspapers want you to sign in?

The obvious, if naive, explanation is that you need to answer `are you a subscriber?`. This is essentially the AAA problem:

- Authentication
- Authorisation
- Accounting

But the answer to the question above is **solely** `Authorization`. You don't _really_ need Authentication or Accounting. 

- The question Authentication answers is `Who are you?`. 

- Accounting answers `What and how much are you consuming?`


Sure, some degree of Accounting may be needed for tiered access and so on, but last I checked none of these sites offer anything of the kind.


## So, why do they really need AAA?

I don't **know** the answer. But I can guess. It's because they really do want the answers to the age old questions:

- `Who are you?`
- `Why are you here?`

Either that or they have a bunch of lazy coders.

## Because there's a better model

<img src="/assets/images/blokada_home.png" alt="Blokada Home Screen" height="400" />

Let me introduce you to [Blokada](https://blokada.org/#about). I have been using it for a couple of years to block trackers and ads on my phone. A few months ago, with the WeChat ban in India, I signed up for `Blokada Plus`. This gives me access to the toggle button at the bottom of that screen.

> Blokada works on my phone, on my web browser and my desktop. And it does not know who I am. 

### How does it do that?

By asking the only question it needs to, `Are you a subscriber?`.

And when it does, I provide my unique, randomly generated, `12 character account ID` and all is good.

To access the VPN from my desktop, I log into the web interface with, you guessed it, the account ID. Once logged in, I can generate cryptographic client certificates to use with my VPN client.  

![Blokada Web Login](/assets/images/blokada_web.png)


## What's the catch?

> In theory, this model is no more immune to tracking than any other. 

- Blokada has a payment processor who did receive some of my identity and card information - I didn't choose the  BTC payment option.
- The payment processor could have shared this information with Blokada.
- Blokada could link the "private" account ID with the identity information. 
- Blokada could, right now, be compiling a dossier on every site and app I use.


## BUT...

> In practice, it is possible to make the system pretty rugged. 

Let's imagine a much more private flow for my beloved Guardian.

- I get tired of the half-page banners/want to encourage better journalism and opt to subscribe. 
- The Guardian clears all identifying cookies and session data about me from my browser and their servers.
- I am redirected to a privacy focused payment processor who doubles as an [IDP](https://en.wikipedia.org/wiki/Identity_provider).
  - `UPI, this is not.`
- The payment processor generates a unique ID and sends it to Guardian Towers who then present it to me and make me promise to keep it safely. 
  - This could even be a [long, memorable phrase](https://xkcd.com/936/).
- I log into Guardian on all three devices I own with this unique ID.
- The Guardian verifies that the ID is kosher with our `SuperPrivatePaymentProcessor`.
- I rest easier knowing that [Barney Ronay](https://www.theguardian.com/profile/barneyronay) will never know that I read every one of his articles. 


It's not that hard. We just need to take this shit seriously.