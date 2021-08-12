# **[Selftod | Product Management Resources](https://github.com/effiemanyos/ms3-pmresources)**

**[View Website Live (Heroku)](https://produck-flask-app.herokuapp.com/)**

![web app on different devices](/static/images/mockup.png "web app on different devices")

[Return to README.md Document](/README.md)

-------

# **TABLE OF CONTENTS** 
* [User Stories](#user-stories)
* [Testing & Validation](#testing-&-validation) 

-------

# **USER STORIES**

### **Guest User** (logged out)

√
**As a** *guest user*,               
**I want** to easily understand what is the purpose of the app and for who was it built,          
**so that** I can decide if I should register and start using it or not.

√
**As a** *guest user*,             
**I want** to be able to see examples of resources posted by others,                 
**so that** I can get a sense of how it works and what kind of resources users share.

√
**As a** *guest user*,               
**I want** to be able to quickly register/sign up,                 
**so that** I can start saving/sharing (my own) and discovering (others) PM resources.

√
**As a** *guest user*,                   
**I want** to be able to get in touch with the founders through Selftod's social media,                  
**so that** I can send my suggestions to improve the UX of the app. 

√
**As a** *guest user*,            
**I want** to be able to follow/invite Selftod on social media channels,             
**so that** I can consume their bite-sized product-related content daily.

**Main Pages:**

![home-page](/static/images/home-page.png "home page")

![resources-page](/static/images/rsc-page.png "resources page")

![register-page](/static/images/register.png "register page")

### **Registered User** (logged in)

√
**As a** *registered user*,            
**I want** to easily understand how to perfom all actions I am able to do,               
**so that** I can start contributing to the community of aspiring PMs.

√
**As a** *registered user*,               
**I want** to be able to log in and log out whenever I please,              
**so that** I can control when and from where I want to interact with the app.

√
**As a** *registered user*,             
**I want** to be able search/view resources posted by other registered users/members,               
**so that** I can discover resources.

√
**As a** *registered user*,            
**I want** to be able filter resources by product-related categories,            
**so that** I can view only the ones I am interested in (category-wise).

√
**As a** *registered user*,                    
**I want** to be able to add/search/edit/delete resources (new and already shared),                    
**so that** I can have control of my contribution to the app.

√
**As a** *registered user*,         
**I want** to be able to get in touch with the founders through Selftod's social media,              
**so that** I can send my suggestions to improve the UX of the app. 

√
**As a** *registered user*,          
**I want** to be able to follow/invite Selftod on social media channels,             
**so that** I can consume their bite-sized product-related content daily.

**Main Pages:**

![home-page](/static/images/home-page.png "home page")

![resources-page](/static/images/rsc-page.png "resources page")

![login-page](/static/images/login-page.png "login page")

![my-profile](/static/images/my-profile.png "my profile page")

![add-resource](/static/images/add-rsc.png "add resource")

![edit-resource](/static/images/edit-rsc.png "edit resource")

![delete-resource](/static/images/dlt-rsc.png "delete resource")

### **Admin User** (logged in)

The Admin User has the same access as the Registered User, plus the additional features listed below: 

√
**As an** *admin user*,                            
**I want** to create, update, and delete categories (new and already entered),              
**so that** I can manage how registered users can classified their resources.

√
**As an** *admin user*,                                
**I want** to be able to create, update, and delete featured resources,             
**so that** I can manage what guest users can view on the homepage on monthly basis.

**Main Pages:**

![manage-categories](/static/images/mg-categories.png "manage categories")

![add-category](/static/images/add-category.png "add category")

![edit-category](/static/images/edit-category.png "edit category")

![delete-category](/static/images/dlt-category.png "delete category")

# **TESTING & VALIDATION**

### [Link Checker](https://validator.w3.org/checklink)
- To check that all the links within the web application are not broken and working perfectly.

**Testing & Final Results:**

- There are no link errors or warnings

### [Chrome DevTools: Lighthouse](https://developers.google.com/web/tools/lighthouse)

- To test the web application's accesibility and performance on desktop and mobile, Google Lighthouse was used for both cases.

**Testing & Final Results:**

- **Desktop**: Not the desired outcome, there is still room for improvement

- **Mobile**: Not the desired outcome, there is still for improvement

### [JavaScript: JSHint](https://jshint.com/)

**Testing & Final Results:**

- **script.js**: No errors or warnings found

### [CSS: W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
- The CSS code of this project was validated by copying/pasting the code from the styles.css file to the "Validate by Direct Input" tab.

**Testing & Final Results:**

- **style.css**: No errors or warnings found

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- The HTML code of this project was validated by copying/pasting each screen's code to the "Validate by Direct Input" tab. Keep in mind that the W3C Validator cannot understand the Jinja templating syntax, so if there is any error or warning related to this, please ignore.

**Testing & Final Results:**

- **base:** No errors or warnings found
- **home:** No errors or warnings found
- **resources:** No errors or warnings found
- **login:** No errors or warnings found
- **register:** No errors or warnings found
- **profile:** No errors or warnings found
- **add resource:** No errors or warnings found
- **edit resource:** No errors or warnings found
- **categories:** No errors or warnings found
- **add category:** No errors or warnings found
- **edit category:** No errors or warnings found
- **404 & 500:** No errors or warnings found

### [Python: Extendsclass](https://extendsclass.com/python-tester.html)

**Testing & Final Results:**

- No syntax errors were detected
