YAN-SHAN-PHAN-WU
================

This project is to make an app (a website) that can store messages at locations (GPS).  <br>

The main  page displays option, SCAN, NEWMESSAGE, LOGIN (to be implemented)  <br>
The SCAN page displays all messages stored at that coordinate. <br>
The NEW page allows you to create a new message at that coordinate. <br>
The LOGIN (to be implemented) <br>


It uses HTML5 Geolocation API to get lat/lon and that works fine. 

<h3>I rewrote HTML/javascript, should be good. </h3>
<h4>app.py is rewritten. </h4> 


<br>1. Login page (or redirect to register for an account page)- info: first and last name, password, age (we should set an age limit because this requires gps and might affect safety or something), email (or possibly login with facebook)
<br>2. after login, transfer to a default "browsing" page with a gmap of 100m radius. On the map: clicking on a location with the red pin will show name of user and name of file/what the message is. Since we want to pretty specific with our locations (e.g. not Times Square but 42nd street, 6th ave or something), if there is an overcrowding of those red pins at a popular location like Times Square, we can have a button where they can redirect to another page with a mini newsfeed of who dropped what files/wrote what message in that general area, listed with their specific street intersections
<br>3. "check-in" page with upload button for files/write a message button
<br>4. Edit/view account details (maybe a history of what, when, where they dropped a file off/wrote a message and a history of what the user has picked up and its details)
<br>5. Main feed (kind of like Twitter/Facebook/Tumblr), where all the users using our project will have their activity posted up. Like "Brian Yan was at Times Square and he said-- "i'm mad cool" " (this might have some privacy/safety issues though so maybe include an option for the user to choose whether or not they want to publish their activity... i'm pretty sure shan and i thought of another solution for this problem but i dont remember what it was)

<br>*also, we're going to add a dropdown menu, that can allow the user to navigate between the pages. so there's no real "homepage" except for the login page. it's just that after logging in, the user gets automatically transferred to the "browsing" page
