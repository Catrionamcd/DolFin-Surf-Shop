# Manual Testing
Manual testing throughout the site. Steps and results are as follows.

## User Stories
### Epic - Registration and User Accounts

- User presented with homepage with cards for the different categories of product on sale on the site. They also should be presented with a side bar menu.

![alt text](assets/test-documentation/Test-Homepage.png)

#### Testing Steps: 
- Click on Login/Register to set up a new user with email, name and password.

![alt text](assets/test-documentation/Test-SignUp-2.png)

- Make sure the password is valid.

![alt text](assets/test-documentation/SignUp-Password.png)

- Make sure the user receives an email for verification.

![alt text](assets/test-documentation/Verification-Email.png)

![alt text](assets/test-documentation/Confirmation-Email.png)

- Ensure that the user can then login and out easily.

- If incorrect username or password used, error message displayed.  

![alt text](assets/test-documentation/Test-SignIn-Error.png)

- Once the user is loggged in the user name should appear on the top right hand side of the navigation bar.

Pass/Fail : **Pass**

### Epic - View and Navigation	

Navigation - check that all navigation links work as expected.
#### Testing Steps:

- Without logging in click on the links in the navbar.
- Enter nothing in search criteria to get an error message.

![alt text](assets/test-documentation/Error-Search.png)

- Click on Card Category to see all products for that category even if the shopper is not logged in.

![alt text](assets/test-documentation/Test-Products-NoLogin.png)

Pass/Fail : **Pass**

- Click on Category and/or sub-category in the side bar to filter products even more.

![alt text](assets/test-documentation/Search-SubCategory.png)

- Click on a product image to view an individual product details, get a more detailed description, product size, colour depending on the type of product.

![alt text](assets/test-documentation/Test-Product-Detail.png)

-  View commonly purchased product with the product on view. See other product or products that were bought along the product on view.

![alt text](assets/test-documentation/Bought-Together.png)

- View customer reviews on the product
- Click on Home or Company logo to return to homepage.

Pass/Fail : **Pass**

### Epic - Filter,  Sort and Search	
- Enter different filters on products such as categories or brands.

![alt text](assets/test-documentation/Filter-Brands.png)

- Sort products by price, A-Z product name.

![alt text](assets/test-documentation/Sort-LowToHigh.png)

- Search for a product by name or description within a category chosen from the menu.

![alt text](assets/test-documentation/Sort-Desc.png)

- Easily see what I've searched for and the number of results.

Pass/Fail : **Pass**

### Epic - Purchasing and Checkout	
- Easily select the quantity and size.
- Change size and/or quantity if needed.
- Add the product on view to the shopping bag.

![alt text](assets/test-documentation/Test-ShoppingBag.png)

- Keep shopping for more products by clicking the 'keep shopping tab'.

![alt text](assets/test-documentation/Test-AddBag.png)

- Purchase a gift card for a particular value

![alt text](assets/test-documentation/Purchase-GiftCard.png)

- View items in my bag to be purchased to identify the total cost of their purchase.
- Adjust the quantity of individual items in my bag.
- View running total of items and total cost in shopping bag.
- Once happy with the order go to secure checkout.
- Enter user details in checkout screen.

![alt text](assets/test-documentation/Checkout-Screen.png)

- Easily enter my payment information. 

![alt text](assets/test-documentation/Payment-Info.png)

- If incorrect detial are entered display an error message.

![alt text](assets/test-documentation/Invalid-Card.png)

- View an order confirmation after checkout.

![alt text](assets/test-documentation/Order-Confirmation.png)

- Receive an email confirmation after checking out to have the confirmation of what they have purchased.
- Order details are processed through Stripe 

![alt text](assets/test-documentation/Charge-Success.png)

- The order history can be seen for this users profile.

![alt text](assets/test-documentation/Test-Profile-History.png)

- Check adding reviews to a product.

![alt text](assets/test-documentation/Test-Reviews.png)

- Test editing and deleting a review.

![alt text](assets/test-documentation/Edit-Review.png)

![alt text](assets/test-documentation/Edit-Review-Change.png)

![alt text](assets/test-documentation/Delete-Comment.png)

Pass/Fail : **Pass**

### Epic - Admin and Shop Management	
- Add a product to the site.
- Edit\Update a product, change product prices, description, images etc.

![alt text](assets/test-documentation/Edit-Obsolete.png)

- Delete a product that has no orders attached.

![alt text](assets/test-documentation/Delete-Product.png)

- Ability to make a product obsolete so that is no longer available for sale on the site.
- Ability to add a discount to a particular category of productso offer sale discount to the customers.

Pass/Fail : **Pass**

# 404/500 Custom Error Screens

If a 404 error occurs a custom Dolfin Surf Shop screen will be displayed with the link to direct the shopper back to the site.

![alt text](assets/documentation/404-Error-Screen.png)

Similarly when a 500 error occurs:

![alt text](assets/documentation/500-Error-Screen.png)

# Code Validation

## CSS Validation

![alt text](assets/code-validation/CSS-Validation.png) 

## HTML Validation

![alt text](assets/code-validation/HTML-Validation.png)
![alt text](assets/code-validation/Bag-Html.png)
![alt text](assets/code-validation/Checkout-Html.png)
![alt text](assets/code-validation/Products-Html.png)
## Python



- Bag/Apps.py

![alt text](assets/code-validation/Bag-Apps-Py.png)

- Bag/Context.py

![alt text](assets/code-validation/Bag-Context-Py.png)

- Bag/Urls.py

![alt text](assets/code-validation/Bag-Urls-Py.png)

- Bag/Views.py

![alt text](assets/code-validation/Bag-Views-Py.png)

- Bag/templatetags/bag_tools.py

![alt text](assets/code-validation/Bag-Tools-Py.png)

- checkout/Admin.py

![alt text](assets/code-validation/Checkout-Admin-Py.png)

- Checkout/Apps.py

![alt text](assets/code-validation/Checkout-Apps-Py.png)

- Checkout/Forms.py

![alt text](assets/code-validation/Checkout-Forms-Py.png)

- Checkout/Models.py

![alt text](assets/code-validation/Checkout-Models-Py.png)

- Checkout/Views.py

![alt text](assets/code-validation/Checkout-Views-Py.png)

- Checkout/Webhooks_Handler.py

![alt text](assets/code-validation/Checkout-Webhooks-Handler-Py.png)

- Checkout/Webhook.py

![alt text](assets/code-validation/Checkout-Webhook-Py.png)

- Home/Apps.py

![alt text](assets/code-validation/Home-Apps-Py.png)

- Home/Urls.py

![alt text](assets/code-validation/Home-Urls-Py.png)

- Home/Views.py

![alt text](assets/code-validation/Home-Views-Py.png)

- Products/Admin.py

![alt text](assets/code-validation/Products-Admin-Py.png)

- Products/Apps.py

![alt text](assets/code-validation/Products-Apps-Py.png)

- Products/Forms.py

![alt text](assets/code-validation/Products-Forms-Py.png)

- Products/Models.py

![alt text](assets/code-validation/Products-Models-Py.png)

- Products/Urls.py

![alt text](assets/code-validation/Products-Urls-Py.png)

- Products/Views.py

![alt text](assets/code-validation/Products-View-Py.png)

- Products/Widgets.py

![alt text](assets/code-validation/Products-Widgets-Py.png)


- Profiles/Apps.py

![alt text](assets/code-validation/Profiles-Apps-Py.png)

- Profiles/Forms.py

![alt text](assets/code-validation/Profiles-Forms-Py.png)

- Profiles/Models.py

![alt text](assets/code-validation/Profiles-Models-Py.png)

- Prodfiles/Urls.py

![alt text](assets/code-validation/Profiles-Urls-Py.png)

- Profiles/Views.py

![alt text](assets/code-validation/Profiles-Views-Py.png)

- Settings.py

![alt text](assets/code-validation/Settings-Py.png)

This refers to the following lines which are built in to Django settings. This is a known Django error and it is acceptable not to force a line break in these cases.

## Javascript

- checkout/static/js/stripe_element.js

![alt text](assets/code-validation/Checkout-JS.png)


- main.html- embedded js

![alt text](assets/code-validation/Menu-JS.png)
