# E-Commerce Auction Site

This project is an eBay-like e-commerce platform that allows users to create auction listings, place bids on listings, comment on listings, and manage a personal watchlist of items they are interested in.

## Features

### User Authentication
- **Registration:** Users can create a new account.
- **Login/Logout:** Users can log in and out of their account.
- **Authenticated Experience:** Different content is displayed based on whether the user is signed in.

### Auction Listings
- **Create Listings:** Users can create new auction listings with a title, description, starting bid, image (optional), and category (optional).
- **Active Listings Page:** The homepage shows all active auction listings, displaying the title, current price, description, and image (if available).
- **Listing Page:** Each listing has a detailed page with all relevant information, such as the current highest bid, description, and image.

### Bidding
- **Place Bids:** Authenticated users can place bids on active listings. Bids must be at least the starting bid or greater than the current highest bid.
- **Close Auction:** The listing creator can close the auction, marking the highest bidder as the winner. Once closed, the auction is no longer active.
- **Winning Notification:** If a user wins an auction, they are notified on the listing page.

### Comments
- **Add Comments:** Users can leave comments on a listing. All comments are displayed on the listing page.

### Watchlist
- **Add to Watchlist:** Users can add listings to their personal watchlist.
- **Watchlist Page:** Users can view all the items they have added to their watchlist and navigate to their respective listing pages.

### Categories
- **Browse by Category:** Users can view a list of categories and see all active listings within a specific category.

### Admin Interface
- **Manage Listings, Bids, and Comments:** Administrators can view, add, edit, or delete listings, bids, and comments via the Django admin panel.

## Getting Started

### Prerequisites
Ensure that you have Python installed and Django set up in your environment.

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
2.**Navigate to the project directory:** 
cd commerce

3.**Apply database migrations** 
python manage.py makemigrations auctions
python manage.py migrate


4.**Run Development Server** 
python manage.py runserver

5. **Access the site:**
Visit http://127.0.0.1:8000/ in your web browser.

## Models
The application uses the following models:

User: Inherits from Django's AbstractUser, representing users of the platform.
Listing: Represents an auction listing with fields for title, description, starting bid, image, and category.
Bid: Represents a bid placed on a listing.
Comment: Represents a comment made on a listing.
Watchlist: Allows users to track their favorite listings.

## How to Use
Register: Create an account or log in.
Create Listing: Navigate to the create listing page to post an auction.
View Listings: Explore active listings on the homepage or browse by category.
Bid on Listings: Place bids on items of interest.
Watchlist: Add items to your watchlist for easy tracking.
Close Auction: If you created the listing, you can close the auction and declare a winner.
Leave Comments: Discuss listings by leaving comments on the listing page


