# **[Selftod | Product Management Resources](https://github.com/effiemanyos/ms3-pmresources)**

**[View Website Live (Heroku)](https://produck-flask-app.herokuapp.com/)**

![web app on different devices](/static/images/mockup.png "web app on different devices")

[Return to README.md Document](/README.md)

-------

# **TABLE OF CONTENTS** 
* [User Stories](#user-stories)
* [Testing & Validation](#testing-&-validation) 
* [Bugs & Fixes](#bugs-&-fixes)
* [Further Testing](#further-testing)

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

### **Guest User** (logged out)

##  **Testing and Validation**
### [Link Checker](https://validator.w3.org/checklink)
- To check that all links are working and not broken. 
- [Link Validation Test](/documentation/images/validator_screenshots/linkchecker.png)
   - Issue with https://fonts.googleapis.com/ in the header of the base template but this directly copied and pasted from the Google Fonts website to use a font. Therefore this can be safely ignored.
   - Issue with Linkedin link was manually checked and resolved.
   - Issue with Instagram link was manually checked and resolved.
- Final version has no other link errors or warnings.

### Lighthouse (Google dev tool)
- To test the accessibility and performance of the website. 
- Final versions: 
   - [Lighthouse report desktop ](/documentation/images/validator_screenshots/lighthouse_desktop.png)
   - [Lighthouse report mobile ](/documentation/images/validator_screenshots/lighthouse_mobile.png)

### [Responsinator](http://www.responsinator.com/)
- To test the responsiveness of the live website and functionalities on different size mobile devices.
- Final version: 
   - [Mobile view ](/documentation/images/validator_screenshots/responsinator_mobile.png)
   - [Tablet view ](/documentation/images/validator_screenshots/responsinator_tablet.png)

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
- Final version: [Am I Responsive ](/documentation/images/validator_screenshots/am_i_responsive_design.png)

### JavaScript
- [JSHint](https://jshint.com/)
   - [Test JavaScript Validation](/documentation/images/validator_screenshots/jshint_test.png)
   - [Final JavaScript Validation](/documentation/images/validator_screenshots/jshint_final.png)
   - Final version - addressing errors and warnings: 
      - Warning for ''let' is available in ES6 (use 'esversion: 6'). Can be safely ignored. If add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored. 
- [JSEsprima](https://esprima.org/)
   - [Final JavaScript Validated](/documentation/images/validator_screenshots/js_esprima_final.png)

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CCS code of the project pasting code in by direct input method.
- Final version - addressing errors and warnings: 
   - The Validator states there is an error with regards to the "text-decoration-thickness" but this is acceptable according to [w3.org](https://www.w3.org/TR/css-text-decor-4/#propdef-text-decoration-thickness) and [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-thickness). This property, sets the stroke thickness of underlines, overlines, and line-throughs specified on the element with text-decoration-line, and affects all decorations originating from this element even if descendant boxes specify a different thickness. Therefore, it can be safely ignored.
   - 8 warnings relating to custom colour variables. The W3C CSS validator cannot parse :root variables. Therefore it can be safely ignored.
   - Warnings for vendor extensions suggested by AutoPrefixer is valid to ensure CSS styles can work across multiple browsers, can be safely ignored.
- [Final CSS Validation](/documentation/images/validator_screenshots/css_validator_final.png)

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- The HTML code of this project was validated by copying/pasting each screen's code to the "Validate by Direct Input" tab. Please note that the W3C Validator for HTML cannot understand the Jinja templating syntax, so if there is any error or warning related to this, it can be ignored.

**Testing & Final Results:**

- **Resources:** No error or warnings
- **Register:** No error or warnings
- **Profile:** No error or warnings


### Python
- [Extendsclass](https://extendsclass.com/python-tester.html) - No syntax errors
   - [Final Python Validated](/documentation/images/validator_screenshots/python_extendsclass_final.png)
- [PEP8 Online](http://pep8online.com/) - Pythoon file is PEP8 compliant
   - [Final Python Validated](/documentation/images/validator_screenshots/python_pep8online_final.png)

### Google Dev Tool 
- To check for errors in JavaScript code
- Final version: no errors or warnings 

### Browser Compatibility
To ensure a broad range of users can successfully use this site, I tested it across the 6 major browsers in both desktop and mobile configuration. See the [Browser Compatibility Table](/documentation/images/validator_screenshots/browser_compatibility_table.png) for more detail. The following browsers were tested:
- Chrome
- Firefox 
- Safari
- Opera
- Edge
