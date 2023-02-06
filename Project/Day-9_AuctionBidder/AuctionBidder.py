from logo import logo

print(logo)

shouldContinue = False

auctionBidder = {}


def highestBidder(bidder):
    highestBidder = 0
    highestName = ""

    for key in bidder:
        if bidder[key] > highestBidder:
            highestBidder = bidder[key]
            highestName = key

    print(f"The winner is {highestName} and the bid is ${highestBidder}")


while not shouldContinue:
    name = input("What is your name: ")
    price = int(input("What is your bid :$"))

    auctionBidder[name] = price
    finnish = input("Are there any other bidder ? type \'yes\' or \'no\': ")
    if finnish == "no":
        shouldContinue = True
        highestBidder(auctionBidder)
