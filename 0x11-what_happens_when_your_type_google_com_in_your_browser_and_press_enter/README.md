# What happens when you type "https://www.google.com” in your browser and press Enter

### Hey there, Just a learner like you! Ever wondered what happens behind the scenes when you hit the Enter key after typing in a URL on your browser; sit with me while we go together to see what’s up by taking a short dive into the following terms: DNS, TCP/IP, firewalls, HTTPS/SSL, load-balancers, web servers, application servers, and databases each of which plays an important role in our access to the internet; “this blog post” included.

### In the digital age, the internet has become an integral part of our lives, enabling endless access to information and services with just a few clicks. All these won’t be possible without the terms mentioned before and which will be explained below; let our adventure begin:

## DNS Request (Finding the Unknown Address):

### Domain Name System commonly called (DNS). They say the computer speaks in numbers, yes? So when you type the URL “google.com” into your browser, it first needs to translate the human-readable domain name (website as it is commonly called) into an IP address (numbers!!!) . Your browser sends a DNS query(request for directions to a website) to a DNS resolver(it’s job is to find website addresses); which then searches for the corresponding IP address associated with the domain human-readable name you input in your browser.

## TCP/IP (Exploring the Cyber Highway):

### Once your device figures out where to go using the IP address from the DNS resolver, it’s uses a vehicle called Transmission Control Protocol (TCP) to get to the website’s home(website’s server). TCP is like the guardian angel of your data packets(let’s say this is a virtual envelope/mail carrying your online messages and information), making sure they all arrive safely and in the right order; like your exact coffee order at your favorite shop. The Internet Protocol (IP) acts like a digital GPS, deciding the best route for your online messages to reach exactly where they need to go.

## FIREWALL(The GateKeepers):

### Before establishing a connection, the request may encounter firewalls; firewalls are like the bouncers at the “google.com”cyber nightclub, making sure only the coolest cats get inside while keeping the riffraff‘s’ out, in technical words they act as barriers to filter and monitor incoming and outgoing network traffic. Firewalls enforces security policies to protect against unauthorized access and potential threats.

## HTTPS/SSL (Securing the Websites Walls):

### It is a cold world out there, yeah? Well Secure Sockets Layer (SSL) got you covered like your warm blankets on a cold night. The SSL simply encrypt the data exchanged between the browser and the server, ensuring confidentiality and integrity. The server presents its digital certificate to authenticate its identity to the browser so basically the “Connection not secure” you see when you are about to visit some websites, that is your browser not able to verify the SSL certificate of the website you are requesting to visit and warning you. This warning from your browser is because a website which is not secure can steal your private details(Passwords, credit card details, even go as far as phishing your device.)

## Load-Balancer(Finding the balance):

### For big websites like Google, they have lots of servers in their internet home base working together to handle all the people trying to visit. Imagine a load balancer as the traffic cop directing cars to different lanes on the highway. It spreads out the traffic evenly so no server gets overwhelmed. This helps keep everything running smoothly, making sure everyone gets to their destination fast, and the website stays reliable even when lots of people are using it.

## Web Server (The Mixer):

### When you click on a link or type in a website, your request heads to a digital center known as a web server like Apache or Nginx; it processes the request and retrieves the requested web page. The web server generates a response containing the HTML, CSS, JavaScript, and other files required to render the website page on your browser; see it as a music producer mixing and mastering together to give you your favorite songs.

## Application Server(Making it more Organized):

### In more complex web applications, an application server may be involved in handling dynamic content generation and business logic. Common application servers include Tomcat, Django, or Node.js.

### So let’s see it like this; imagine you’re playing a game online with your friends. The application server is like the referee, making sure everyone follows the rules and keeps track of what’s happening in the game. It’s also handling things like storing your scores, updating the game world when you move around, and making sure everything runs smoothly so you can keep playing without any glitches.

### Technically, these servers execute server-side code, interact with databases, and generate dynamic content tailored to the user’s request.

## Database(The Storage Chest):

### Think of it as a digital warehouse storing all the important stuff like your user info, product catalogs, or transaction records. Databases like MySQL, PostgreSQL, or MongoDB keep everything organized and ready to go when the website needs it.

### So if the requested content involves data retrieval or manipulation, the application server may communicate with a database server to provide you the data needed.

### So, there you have it! That’s the adventure of what really happens when you type “https://www.google.com" into your browser and press Enter. From translating human-readable addresses to digital numbers, to navigating through cyber traffic jams and ensuring your online safety, it’s a wild ride! Just remember, behind every clicks lies a whole world of servers, databases, and security measures, all working together to make your internet experience smooth and enjoyable. Keep exploring the digital world, and never stop wondering about the wonders of the web!

#### Author: Slonjoh
#### Date: 11/02/2024
