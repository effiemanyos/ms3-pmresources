# **[Selftod | Product Management Resources](https://github.com/effiemanyos/ms3-pmresources)**

## **Python & Data Centric Development Milestone Project 3**

### **Project Overview**

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

**Main Technologies Required:** HTML, CSS, JavaScript, Python+Flask, MongoDB, Libraries, External APIs

**[View Website Live (Heroku)](https://effiemanyos.github.io/milestone-project-one/)**

![web app on different devices](/static/images/placeholder.jpg "web app on different devices")

<br>

-------

<br>

# **TABLE OF CONTENTS** 

- [Project Overview](#project-overview "Project Overview") ⬆
- [UX Design](#ux-design "UX Design")
  - [Strategy Plane](#strategy-plane "Strategy Plane")
    - [Target Audience](#target-audience "Target Audience")
    - [User Persona](#user-persona "User Persona")
    - [User Needs](#user-needs "User Needs")
    - [User Goals](#user-goals "User Goals")
    - [User Stories](#user-stories "User Stories")
    - [Jobs To Be Done](#jobs-to-be-done "Jobs To Be Done")
    - [User Flow](#user-flow "User Flow")
    - [Business Goals](#business-goals "Business Goals")
  - [Scope plane](#scope-plane "Scope plane")
    - [User Requirements](#user-requirements "Requirements")
    - [User Expectations](#user-expectations "Expectations")
    - [Acceptance Criteria](#acceptance-criteria "Acceptance Criteria")  
    - [Existing Features](#existing-features "Existing Features")
    - [Future Iterations](#future-iterations "Future Iterations")
    - [Product Roadmap](#product-roadmap "Product Roadmap")
  - [Structure Plane](#structure-plane "Structure plane")
    - [App Structure](#app-structure "App Structure")
    - [Data Structure](#data-structure "Data Structure")
    - [Planned Structure](#planned-structure "Planned Structure")
    - [Future Additions](#future-additions "Future Additions")
  - [Skeleton Plane](#skeleton-plane "Skeleton Plane")
    - [Wireframes](#wireframes "Wireframes")
  - [Surface Plane](#surface-plane "Surface Plane")
    - [Typography](#typography "Typography")
    - [Color Scheme](#color-scheme "Color Scheme")
    - [Logo Variants](#logo-variants "Logo Variants")
    - [Imagery](#imagery "Imagery")
- [Technologies Used](#technologies-used "Technologies Used")
    - [Languages](#languages "Languages")
    - [Libraries](#libraries "Libraries")
    - [Tools](#tools "Tools")
    - [Design](#design "Design")
- [Testing](#testing "Testing")
- [Deployment](#deployment "Deployment")
- [Credits](#credits "Credits")
- [Acknowledgements](#acknowledgements "Acknowledgements")

<br>

-------

# **UX DESIGN**  

## **Strategy Plane** 

### **Target Audience**
- Recent University/College Graduates (Tech & Non-Tech Backgrounds)
- Aspiring Product Managers (Entry/Mid-Level Professionals [Other Backgrounds])
- Product Enthusiasts (Curious & Interested Professionals)
- Young Tech Startup Owners (Digital Products, SaaS, Apps, Web Apps)
- Young Business Founders (Services, eCommerce, Agencies, Consultancy)
- Entry/Mid-Level Product Managers (Interns, Associates, PMs)
- Professionals Already Transitioning Into Product Management

### **User Persona**

According to our user/market research:
- Most of them utilize the web-based app on their desktops and/or laptops during work and/or study time.
- The vast majority of them are between 22-32 years old, which indicates they are mostly entry/mid-level.
- Most of them have at least a bachelor's degree; however, some have masters in business or related fields.
- They feel passionate about tech and innovation, they are customer-obssesed and love solving problems.
- They are mainly from English-speaking countries: Ireland, England, Scotland, United States, Australia.
- They are very interested in digital products, user experience, customer behaviour, and optimization.
- Within the tech adoption curve of Rogers, most of them are considered 'innovators' and 'early adopters'.
- The vast majority finds themselves under the constraints of a tight/no budget to spend on studies.
- They do not have time to invest in long courses or even to research what sources of info are the best.
- Their favourite brands and tools are: Apple, Notion, Miro, Figma, Canva, Trello, Jira, Asana, Amazon.

### **User Needs**

These are some crucial **user pain points and struggles** worth mentioning:

1. **Lack of Trust** <br>
Entry level professionals, our main users, do not know how to differentiate between high-quality content and poor/fake Product Management content on the internet, as they do not have previus professional experience in the field; moreover, most of our users do not have a mentor guiding them in their journey.
2. **Quantity Over Quality** <br>
There is too much information on the internet, and most sources share very vague, superficial or inaccurate information about Product Management. The spread of misleading and erroneous information can lead newbies to start their Product Management careers with the wrong foot, causing horrible disasters in the launch of new products and/or features. 
3. **Overwhelming & Exhausting** <br>
It is overwhelming and exhausting for users to navigate through all those online resources (too many options to choose from), while also trying to find the right information from the right source without having to consult friends or colleagues (assuming they know some people in the field).
4. **Lack of Time** <br>
There is too much going on in the users' lives at the moment (esp. during the global pandemic) that they do not have the time to search for the information themselves because it is proven that it takes a lot of time to do the research every time they need to know about an specific topic. 
5. **Fear of Missing Out (FOMO)** <br>
During the user research, most users have also shared that they constantly feel that they are missing out on great tips and valuable content from high-quality resources (esp. from Fortune 100 companies, product-related book authors, mentors, subject matter experts, experienced PMs).
6. **No Official PM Studies** <br>
At the moment, no official Product Management studies are offered by universities or colleges, and if they are  Users are looking for cost-effective bootcamps, workshops, cohorts, mentors, and online courses to learn more about this relatively new field in the tech industry.

### **User Goals**
- View product-related resources shared by like-minded professionals in Selftod community. 
- View, search, filter, discover, share, edit, delete resources created by them and others.
- Perform the actions right above from anywhere, via any type of digital device or browser.
- View featured resources on a monthly basis shared by the admin of Selftod's community.
- Learn about PM at their own pace (in their own time/schedule), customized to their needs.
- Discover new valuable sources of information about the field which are highly recommended.
- Save time by going straight to the app to look for specific information urgently needed.
- Find the right sources of information to learn PM by themselves with the required guidance.
- Be up-to-date with the latest frameworks, tools, and techniques that people are applying.

### **User Stories**

👉🏼  **Guest User** (logged out)

**As a** *guest user*,               
**I want** to easily understand what is the purpose of the app and for who was it built,          
**so that** I can decide if I should register and start using it or not.

**As a** *guest user*,             
**I want** to be able to see examples of resources posted by others,                 
**so that** I can get a sense of how it works and what kind of resources users share.

**As a** *guest user*,               
**I want** to be able to quickly register/sign up,                 
**so that** I can start saving/sharing (my own) and discovering (others) PM resources.

**As a** *guest user*,                   
**I want** to be able to get in touch with the founders through Selftod's social media,                  
**so that** I can send my suggestions to improve the UX of the app. 

**As a** *guest user*,            
**I want** to be able to follow/invite Selftod on social media channels,             
**so that** I can consume their bite-sized product-related content daily.

👉🏼  **Registered User** (logged in)

**As a** *registered user*,            
**I want** to easily understand how to perfom all actions I am able to do,               
**so that** I can start contributing to the community of aspiring PMs.

**As a** *registered user*,               
**I want** to be able to log in and log out whenever I please,              
**so that** I can control when and from where I want to interact with the app.

**As a** *registered user*,             
**I want** to be able search/view resources posted by other registered users/members,               
**so that** I can discover resources.

**As a** *registered user*,            
**I want** to be able filter resources by product-related categories,            
**so that** I can view only the ones I am interested in (category-wise).

**As a** *registered user*,                    
**I want** to be able to add/search/edit/delete resources (new and already shared),                    
**so that** I can have control of my contribution to the app.

**As a** *registered user*,         
**I want** to be able to get in touch with the founders through Selftod's social media,              
**so that** I can send my suggestions to improve the UX of the app. 

**As a** *registered user*,          
**I want** to be able to follow/invite Selftod on social media channels,             
**so that** I can consume their bite-sized product-related content daily.

👉🏼  **Admin User** (logged in)

The Admin User has the same access as the Registered User, plus the additional features listed below: 

**As an** *admin user*,                            
**I want** to create, update, and delete categories (new and already entered),              
**so that** I can manage how registered users can classified their resources.

**As an** *admin user*,                                
**I want** to be able to create, update, and delete featured resources,             
**so that** I can manage what guest users can view on the homepage on monthly basis.

### **Jobs To Be Done**
- XXX
- XXX
- XXX
- XXX
- XXX

### **User Flow**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Business Opportunity**

- Growth demand for Product Managers → More and more companies are looking to recruit product managers.
- Golden age of PM → Companies have realized that the most successful businesses are product-oriented.
- Tech gap in Irish market → 42% of Irish people describe themselves as being ‘below avg.' for digital skills.
- Boom in tech industry worldwide → Specially after COVID-19, most businesses were forced to go online.
- [*The Product Economy Is Increasing The Need For Product Managers by Carlos Gonzalez De Villaumbrosia*](https://www.forbes.com/sites/forbesbusinesscouncil/2020/12/10/the-product-economy-is-increasing-the-need-for-product-managers/?sh=30654bfa6253)

> (^) With this business model, users will benefit from other people's free contributions (i.e. crowdsourced information - like Waze).             
> (^) When Selftod already has enough data entered by registered users/admin, we will start charging businesses to place ads.           
> (^) The app will always be free for users (restricted to guest users) as they are the ones that contribute the most to its growth.      

### **Business Goals**
- XXX
- XXX
- XXX
- XXX

<br>

[Back to Table of Contents](#table-of-contents)

<br>

## **Scope Plane** 

### **User Requirements**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Acceptace Criteria**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Existing Features**

👉🏼  **Home Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Resources Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Add Resource Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Edit Resource Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Categories Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Add Category Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Edit Category Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **My Profile Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Register Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Log In Page**
- XXX
- XXX
- XXX
- XXX

👉🏼  **Log Out Function**
- XXX
- XXX
- XXX
- XXX

### **Future Iterations**
1. Users will be able to permanently delete their accounts if desired
2. Users will be able to bookmark their favourite resources (theirs/others)
3. Users will be able to view their favourite resources in a dedicated page
4. Users will be able to share their favourite resources on social channels
5. Users will be able to change their own password if they have forgotten it
6. Users will be able to change their registered email address if desired
7. Users will be able to hide the preferred resources for themselves only
8. Users will be able to add/update/delete a profile picture to their accounts
9. Users will be able to subscribe to a weekly notification w/popular resources
10. Admin will be able to update/delete other users' entries to mantain quality
11. Users will be able to request the addition of a category through a form

### **Product Roadmap**

The estimated roadmap after the launch of the MVP is the following: 

|NOW|NEXT|LATER|
|----|----|----|
|1|4|6|
|2|5|7|
|3|8|9|
|10|||
|11|||

These features have been chosen after we applied the Moscow method as a prioritization technique to decide on what to build next, which is influenced by what users need. 

[Back to Table of Contents](#table-of-contents)

<br>

## **Structure Plane**

### **App Structure**

👉🏼  **Admin User | Logged In**

Admin User have access to the following menu:

|Home|Resources|Add New|Categories|My Profile|Log Out|
|----|----|----|----|----|----|
|√|√|√|√|√|√|

Admin User can perfom the following actions within the app:

*Resources*.-
- C > Create or add new product-related resources
- R > Read or search for product-related resources
- U > Update or edit *their own* product-related resources
- D > Permanently delete *their own* product-related resources

*Categories*.-
- C > Create or add new product-related categories (won't be a common action, though)
- R > (*)
- U > Update or edit product-related categories they have previously entered
- D > Permanently delete product-related categories they have previously entered

> The Admin User is the only one that can actually manage categories (C, ~~R~~, U, D).     
> (*) Since the # of categories is less than 12, there is no need for 'Search' functionality

👉🏼  **Registered User | Logged In**

Registered User have access to the following menu:

|Home|Resources|Add New|My Profile|Log Out|
|----|----|----|----|----|
|√|√|√|√|√|

Registered User can perfom the following actions within the app:

*Resources*.-
- C > Create or add new product-related resources
- R > Read or search for product-related resources
- U > Update or edit *their own* product-related resources
- D > Permanently delete *their own* product-related resources

*Categories*.-
- Registered User is not able to CRUD categories at the moment.
- Registered User does not have access to Categories/Add Category/Edit Category.    

👉🏼  **Guest User | Logged Out**

Guest User have access to the following menu:

|Home|Log In|Register|
|----|----|----|
|√|√|√|

Guest User can perfom the following actions within the app:

*Resources*.-
- Guest User is not able to CRUD resources at the moment.
- Guest User do not have access to Resources/Add Resource/Edit Resource.  

*Categories*.-
- Guest User is not able to CRUD categories at the moment.
- Guest User does not have access to Categories/Add Category/Edit Category.

*My Profile*.-
- Guest User does not have access to My Profile/Log Out, just Home/Log In.

### **Future Additions**

Additions to the current structure of the app:

|Home|Resources|Add New|Favourites|Categories|My Profile|Log Out|
|----|----|----|----|----|----|----|
|√|√|√|√|(admin only)|√|√|

> These additions will only be available for Admin User and Registered Users.

### **Data Structure**

**Database** ↓

|Database|
|----|
|myProduckDB|

**Collections** ↓

|Collections|
|----|
|categories|
|resources|
|users|

**Users** ↓

|Collection|Key|Data Type|Collection From|
|----|----|----|----|
|users|_id|ObjectId|
||username|string|
||email|string|
||password|string|

**Resources** ↓

|Collection|Key|Data Type|Collection From|
|----|----|----|----|
|resources|_id|ObjectId||
||resource_title|string||
||resource_icon|string||
||resource_author|string||
||resource_rating|string||
||is_done|string||
||category_name|ObjectId|Categories|
||resource_topic|string||
||source_name|string||
||resource_format|string||
||creation_date|string||
||created_by|ObjectId|Users|
||resource_takeaway|string||
||resource_url|string||

**Categories** ↓

|Collection|Key|Data Type|Collection From|
|----|----|----|----|
|categories|_id|ObjectId|
||category_name|string|

[Back to Table of Contents](#table-of-contents)

<br>

## **Surface Plane** 

### **Typography**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Color Scheme**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Logo Variants**
- Logotype
- Isotype
- Imagetype

### **Imagery**
- XXX
- XXX
- XXX
- XXX
- XXX

[Back to Table of Contents](#table-of-contents)

<br>

# **TECHNOLOGIES USED** 

The following technologies were used during the development and testing of this project:

### **Languages**
- **HTML5** to structure each page and add content.
- **CSS3** to style the elements within each page.
- **JavaScript** to make the website interactive.
- **Python3** to automate specific series of tasks. 

### **Frameworks & Libraries**
- Frameworks → [Materialize V1.0.0](URL)
- Icons → [Font Awesome V5.15.3](URL)
- Main Font → [Google Fonts](https://fonts.google.com/)
- JavaScript Library → [jQuery V3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/)
- Connect Python & Flask to MongoDB → [Pymongo V3.11.4](https://pypi.org/project/pymongo/) & [Flask-PyMongo V2.3.0](https://flask-pymongo.readthedocs.io/en/latest/)
- Construct & Render Pages → [Flask V2.0.1](https://flask.palletsprojects.com/en/2.0.x/)
- Non-Relational Database Hosting Service → [MongoDB Atlas V4.4.6](https://www.mongodb.com/)
- Passwords → [Werkzeug V2.0.1 (WSGI)](https://werkzeug.palletsprojects.com/en/2.0.x/)
- Templating Engine for Python → [Jinja V3.0](https://jinja.palletsprojects.com/en/3.0.x/)
- Hover Over Effects → [Hover.css V2.1.0](https://cdnjs.com/libraries/hover.css/2.1.0)

### **Tools**
- Respository Hosting (Store Repositories) → [GitHub](https://github.com/)
- Main Workspace (IDE: Integrated Development Environment) → [Gitpod](https://www.gitpod.io/)
- Version Control → [Git](https://git-scm.com/)
- Cloud PaaS Enabling Site Deployment → [Heroku](https://heroku.com/)
- Kanban Board → [Trello](http://trello.com/)
- Project Planning → [Notion](https://www.notion.so)
- User-Centric Flows → [Miro](https://miro.com/)
- Check Grammar & Spelling → [Gammarly](https://app.grammarly.com/) 

### **Testing**
- Test/Fix Code → [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
- Web App Responsiveness → [Responsive Viewer](https://www.producthunt.com/posts/responsive-viewer)
- Web App Responsiveness → [Am I Responsive Design](http://ami.responsivedesign.is/#)
- Web App Responsiveness → [Responsinator](http://www.responsinator.com/)
- Mobile-Friendlyness → [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- Web App Performance → [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)
- Validate HTML → [W3C HTML Validator](https://validator.w3.org/)
- Validate CSS → [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- Validate JavaScript → [JS Hint V2.13.0](https://jshint.com/)
- Web App Accessibility Evaluation → [WAVE](https://wave.webaim.org/)
- Validates Tags Correctly Open & Close → [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/)
- Python Code Syntax Checker → [Python Tester](https://extendsclass.com/python-tester.html)
- Check Links → [W3C Link Checker](https://validator.w3.org/checklink)

### **Code Consultations**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Design**
- Visuals & Logo → [Canva](URL)
- Medium/High-Fidelity Mockups & Interactive Design (Prototype) → [Figma](URL)
- Low-Fidelity Mockups & Wireframing → [Balsamiq](URL)
- User-Centric Flows → [Miro](URL)
- Colour Scheme → [Coolors](https://coolors.co/)
- Hex Color Codes (Variants) → [Color Hex](https://www.color-hex.com/)

[Back to Table of Contents](#table-of-contents)

<br>

# **TESTING** 

The entire testing process, issues and bugs found during development, solutions, and final results can be found [here](URL).

- Test User Stories
- Testing & Validation
- Manual Testing
- Bugs & Fixes
- Further Testing

[Back to Table of Contents](#table-of-contents)

<br>

# **DEPLOYMENT**

### **Flask Application**

1. Install Flask - type in terminal: 
    ```
    pip3 install Flask
    ```
2. Now we need to create a few new files. First, our Python file that will be the foundation of our application. You can name it something else, in this case, I used app.py, so type in the terminal: 
    ```
    touch app.py
    ```
3. Next, we will be storing some sensitive data, and we need to hide them using environment variables. You can use the terminal or just create a new file. I used the terminal, so type in the terminal:
    ```
    touch env.py
    ```
4. That file should never be pushed to GitHub, so we need to be able to ignore it somehow, so type in the terminal:
    ```
   touch .gitignore
    ```
5. Double check in the gitignore file that you see "env.py" and "pycache/"
6. Go to the env.py file and add the following:
    ```
    import os
 
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME"
    ```
7. Go to app.py file and import the following:
    ```
    import os
    from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
    from flask_pymongo import PyMongo
    from bson.objectid import ObjectId
    from werkzeug.security import generate_password_hash, check_password_hash
    if os.path.exists("env.py"):
        import env
    ```
8. Create an instance of Flask
    ```
    app = Flask(__name__)
    ```
9. To test your application, tell your app how and where to run your application. Set your IP and PORT environment variables in the hidden env.py file. Make sure to update this to debug=False before the actual deployment of your project.
    ```
    if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
    ```
10. You can now run your application, type in the terminal:
    ```
    python3 app.py
    ```

### **Heroku**

*Workspace Terminal*.-

1. Run **pip3 freeze --local > requirements.txt** to collect any applications and dependencies by creating a requirements.txt file.
2. Run **echo web: python app.py > Procfile** to create the Procfile (what Heroku looks for to know which file runs the app and how to run it).

As you can see, these are the files that Heroku needs to run the app. 
> - First, we need to tell Heroku which apps and dependencies are required to run our web app, via **requirements.txt**,         
> - Next, the **Procfile** is what Heroku looks for to know which file runs the app, and how to run it, so we use the **echo command**.        
> - (^) Remember to delete the second line in Procfile because sometimes it can cause problems when running the app on Heroku.

*Heroku Website*.-

3. Go to **[Heroku](https://dashboard.heroku.com/)**.
4. Log in or create a new account (select Python as your Primary Development Language).
5. You will receive a confirmation email with a magic link to activate your new account.
6. From the dashboard, click on **Create New App**.
7. Type in your app name (choose something unique - don't use spaces, use hyphens instead).
8. Select the right or at least the closest region from the options available.
9. Click on **Create App**.     
10. If you logged in instead, click on your preferred app first.
11. Navigate over to the **Deploy** tab.
12. Go to the **Deployment Method** section.
13. Click on **GitHub**.
14. In the **App Connected to GitHub** section, search for your preferred repository.
15. Click on **Connect**.
16. Go to the **Settings** tab.
17. Scroll down to **Config Vars** section.
18. Click **Reveal Config Vars**.
19. In **Config Vars** section, enter the key and value pairs as per your **env.py** file:

|Key|Value|
|----|----|
|IP|0.0.0.0|
|PORT|5000|
|SECRET_KEY|YOUR_SECRET_KEY (*)|
|MONGO_URI|"mongodb+srv://..." (**)|
|MONGO_DBNAME|YOUR_DB_NAME|

> (*) Generate your secret key on [randomkeygen.com](https://randomkeygen.com/).           
> (**) Used to connect to your database.

20. Then, click on **Hide Config Vars**.
21. Go back to the **Deploy** tab.
22. Scroll down to **Automatic Deploys**.
23. Select the branch you want to deploy from.
24. Next, click on **Enable Automatic Deploys** (-).
25. In **Manual Deploy** section, click on **Deploy Branch**.
25. Upon completion, you will receive a confirmation message saying *“your app was successfully deployed”*.
26. Finally, in the top right corner of the screen, click on **Open App** to view the application.

> (-) Activate this option to automatically rebuild the app when a new *git commit* is pushed.

### **GitHub Pages**

This project was deployed to **GitHub Pages** following these steps:

1. Login to **[GitHub](https://github.com/)**
2. Insert the following **GitHub Repository** name in the **Search Bar** to locate the project: **[effiemanyos/ms3-pmresources](https://github.com/effiemanyos/ms3-pmresources)**
3. Click on that repository to view more details
4. Click on **Settings**, which is located right above the **Gitpod** green button
5. Scroll all the way down to the **GitHub Pages** section
6. Under **Source**, select **Master** in the dropdown menu
7. Select **/(root)** in the tab which is right next to **Branch**
8. Click **Save** (*Note:* the page will automatically refresh)
9. Scroll all the way down again to the **GitHub Pages** section
10. Finally, you can see the link where the site is published highlited with a light green/blue background 

### **Run Project Locally**

1. Login to **[GitHub](https://github.com/)**
2. Insert the following **GitHub Repository** name in the **Search Bar** to locate the project: **[effiemanyos/ms3-pmresources](https://github.com/effiemanyos/ms3-pmresources)**
3. Select **Code** and click on **Download ZIP File**
4. You can extract the file and use it in your local environment once it is downloaded

### **Clone & Fork GitHub Repository**

Additionally, you can either **Clone** or **Fork** this repository ([effiemanyos/ms3-pmresources](https://github.com/effiemanyos/ms3-pmresources)) into your [GitHub](https://github.com/) account by following these guides:
- **[Cloning a Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)**
- **[Fork a Repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)**

[Back to Table of Contents](#table-of-contents)

<br>

# **CREDITS** 
- Preinstalled  Tools (Development) → [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

### **Inspiration**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Code Snippets**
- XXX
- XXX
- XXX
- XXX
- XXX

### **Media**
- Photography → [Unsplash](https://unsplash.com/)
- Illustrations → [UnDraw](https://undraw.co/)

*Hero Image Section:*
- [KW: Studying](https://unsplash.com/photos/1LODZS5mRqs) by [Nicolò Canu](https://unsplash.com/@nick__) taken from [Unsplash](https://unsplash.com/)


[Back to Table of Contents](#table-of-contents)

<br>

# **ACKNOWLEDGEMENTS** 

I would like to thank the following people for their constant support and guidance during my learning process: 
- [Code Institute Slack Community](https://code-institute-room.slack.com/)
- [Adegbenga Adeye (Mentor)](https://www.linkedin.com/in/adegbenga-adeye-psm-i-14003635/)
