# Initial project plan document
The initial project plan should provide a steady framework for our group’s work.

## Course project group information

Start the documentation with identifying information:

- Member name: **Huang Xie**

- student number: 281685

- TUT email: huang.xie@student.tut.fi

- Member name: **Yan Feng**

- student number: 281679

- TUT email: yan.feng@student.tut.fi

- Member name: **Liang Fang**

- student number: 281684

- TUT email: liang.fang@student.tut.fi

- Group name: **bwa-group003**

- GitLab repo URL: https://course-gitlab.tut.fi/bwa-2018/bwa-group003

- Heroku deployment URL: https://cryptic-harbor-29873.herokuapp.com/

## Must have features
Set up an implementation order and timetable for must have features. Decide which features must be implemented before work on others can begin, and setup a deadline for them in the timetable.

Decide initially which tasks (design, research, implement, test,...) are needed to complete each feature. Add them to GitLab’s Issue Board in your repo.


Tasks | Description of must have features | Time of the deadline<br>(DD.MM.YYYY [HH:MM]） 
------------ | ------------- | ------------
Set up development environment |1. Create virtual environment for the project.<br>2. Deploy demo site to Heroku.<br>3. Use GitLab’s issue board for creating tasks  | 31.10.2018
Design | 1. Design of users app.<br>2. Design of users’ profile app.<br>3. Design of friendship app.<br>4. Design of discussion app.<br>5. Design of event app.<br>6. Reorganize the tasks on the GitLab’s issue board.  | 3.11.2018 23:59
implement | 1. Description of the web service data and functionality(Create models including user,users’ profile,friendship,discussions and events.)<br>2. During the web development, we would be aware of project’s progress.<br>3. The gitlab commits should be small and precise.<br>4. often update the deployment on the heroku.<br>5. Update the tasks on on the GitLab’s issue board.  | 28.11.2018 23:59
test | 1. With the validator, validate the Web app codes.<br>2. Deploy our site with DEBUG = False in Django project’s settings.py to Heroku, and test it.  | 07.12.2018 23:59


## Planned +2 features
This subsection in the initial project plan is similar to the “Must have features” subsection above. The same information should be here for the +2 features, as there earlier for the must have features.  

Most important decisions in this subsection is which +2 features the group is interested in implementing. You should decide on a set +2 features which gives you enough +2 stars, even if some are not implemented in the end, or your group receives less than maximum star for some +2 feature.

Remember: _Many of the individual +2 features cannot be easily added to project which has already all the must have features implemented. So, groups should make initial plans on the set of +2 features they plan to implement in the initial project plan document._



Tasks | Description of must have features | Time of the deadline<br>(DD.MM.YYYY [HH:MM] )
------------ | ------------- | ------------
Design | 1. Finnish the high quality of the initial project plan document.  | 3.11.2018 23:59
Implement | 1. mid-project check-in shows faster than expected progress<br>2. Make users, events and discussions searchable<br>3. Email validation on sign-up.<br>4. Reset forgotten password.<br>5. Use separate Django apps for different parts of your project.<br>6. Using Bootstrap for mobile friendliness.<br>7. Use PostgreSQL as database.<br>8. Create the group  | 28.11.2018 23:59
Testing | Unit Testing using Django Test | 07.12.2018 23:59



## Pages and navigation
This is the high level view to your site. Here you have to draw a freeform diagram showing the pages and navigation within your site. Its main function is to ease design discussions within the group, and to communicate your design to the reader. 

First name the web pages of your initial design of the web site site with descriptive names, and draw them as nodes. Then draw the navigation paths between them where needed. Title the navigation paths using the action and the type of user doing the navigation, so it is obvious to reader what the transition between actually means (for example transition from a page showing events to a page page for modifying a single event could be named “User who created the event starts modifying it”. See image 1 for an example. The data and interaction on the web pages is described more closely in the “Needed Django views and templates” subsection.


Get enough detail in this diagram to cover what your group considers are the most important navigation paths in your website. But the diagram should not be an exhaustive documentation of your system, so you should leave what you see as secondary out of it.


![Page Navigation](docs/PageNavigation.png)



## Technological considerations
Here groups handle the technical aspects of their Django implementation. If done correctly, these texts can work as a basis for commenting your code, too.

### Django apps in your Django project
If you plan the implement the one star +2 feature “Use separate Django apps for different parts of your project”, you should design the basic division of functionality apps early on.

![System Components](docs/SystemComponent.png)


### Needed Django models and their attributes
A good start for figuring the needed models is a close reading of “Description of the web app data and related functions”. 

For each model you should state at least:
- Name of the model
- Attributes and their Django types
- A description of the models purpose on your system
- Connections to other models
  ![Models](docs/Models.png)

User: 
The original user model is about the normal users. And the site administrators is extended based on it. 
New users can join the site, and existing users can delete their accounts.  Existing users can login and logout of the system. The users can enter, modify and delete a wide array of personal information about them in to the site.
Users in the site administrator user group have full CRUD permissions on all resources on the site,  they get full permissions to all of the data.



Profile:
User’s profile has both public and private data. Private data is only shown to other logged in users that are friends of this user. The data on the profile page could be edited and saved.
The profile mainly includes the status message, friend list, discussion list, event list and group list.
In the status message, user could update, and to which user’s friends can comment on.



Friendship:
Friendship model lists the friendship requests including the information of senders, recipients, the sending date, the accepting data and the request’s status.
Friendship requests’ status remain open until accepted or declined.



Discussion:
Discussion model contains two aspects: discussion details and the comment issue. In discussion details, the discussion list would exit. The comment addresses the username, date and time and the main content.



Event:
The event model describes the events and event invitation. The event involves the creator’s name, the description, event category, duration for the vent and the place where the event take  place. And the event invitation is for users to invite the other users to join the events.



Groups:
The group has the two aspects: the basic information and discussion. In the basic information, the name and description would be stated in this side. The users who focus on the same subject or could meet place for a group of friends could be divided into the same group.


### URIs
Here you describe how your group’s web site’s URLs are mapped to its resources and views.

URL | Template 
------------ | ------------- 
/ | users/login.html
users/{user_id}/password_change | users/password_change.html
users/{user_id}/password_reset | users/password_reset.html 
users/signup | users/signup.html
users/{user_id}/detail | users/user_detail.html
profiles/{user_id}/home | profiles/profile_home.html 
friendships/{user_id}/home | friendships/friendship_home.html
friendships/{user_id}/request | friendships/friendship_request.html
discussions/{user_id}/home | discussions/discussion_home.html 
discussions/{discussion_id}/detail | discussions/discussion_detail.html
events/{user_id}/home | events/event_home.html
events/{event_id}/detail | events/event_detail.html 
events/{user_id}/invitation | events/event_invitation.html
groups/{user_id}/home | groups/group_home.html
groups/{group_id}/detail | groups/group_detail.html 



### Needed Django views and templates

Name of view or template

For views:  function on the system. Also define when they are called, and with what parameters. What is the output (rendering a template, etc.).


View | Parameters | Rendered Template
------------ | ------------- | ------------
LoginView | -  | users/login.html
PasswordChangeView | user_id  | users/password_change.html
PasswordResetView | user_id  | users/password_reset.html
SignUpView | -  | users/signup.html
UserDetailView | user_id  | users/user_detail.html
ProfileHomeView | user_id  | profiles/profile_home.html
FriendshipHomeView | user_id  | friendships/friendship_home.html
FriendshipRequestView | user_id  | friendships/friendship_request.html
DiscussionHomeView | user_id  | discussions/discussion_home.html
DiscussionDetailView | discussion_id  | discussions/discussion_detail.html
EventHomeView | user_id  | events/event_home.html
EventDetailView | event_id  | events/event_detail.html
EventInvitationView | user_id  | events/event_invitation.html
GroupHomeView | user_id  | groups/group_home.html
GroupDetailView | group_id  | groups/group_detail.html



For templates: a simple sketch or a textual description showing the parts of the page that are be rendered with the template. You should concentrate on what data is shown to users (for example: username as text, list of friendships,,...), and what interaction is possible on the page (for example: “select from list -> click a “Modify” button -> Goto “Modify item” page). You don’t have to define the graphics here.

Template | Description 
------------ | ------------- 
users/login.html | 1. Actions: login.<br>2. Forms: LoginForm. 
users/password_change.html | 1. Actions: change.<br>2. Forms: PasswordChangeForm.
users/password_reset.html | 1. Actions: reset.<br>2. Forms: PasswordResetForm.  
users/signup.html | 1. Actions: signup.<br>2. Forms: SignUpForm. 
users/user_detail.html | 1. Actions: update.<br>2. Forms: UserDetailForm.  
profiles/profile_home.html | 1. Actions: edit, delete.<br>2. Forms: UserDetailForm.<br>3. Lists: discussions, friendships, events, groups.
friendships/friendship_home.html | 1. Actions: delete.  
friendships/friendship_request.html | 1. Actions: delete, accept, decline, ignore. 
discussions/discussion_home.html | -  
discussions/discussion_detail.html | 1. Actions: leave, send message.<br>2. Forms: ChatMessageForm. 
events/event_home.html | - 
events/event_detail.html | 1. Actions: send invitation.<br>2. Forms: EventInvitationForm.
events/event_invitation.html | 1.Actions: delete, accept, decline, ignore.  
groups/group_home.html | -
groups/group_detail.html | 1.Actions: leave. 


### Heroku deployment
Write down the URL of your Heroku app here too.

https://cryptic-harbor-29873.herokuapp.com/

Your plan for the Heroku deployment. 
- Everyone in our group
- Twice a week


## Testing
Here you describe your group’s testing plan for the web site. 

Do you plan to do the +2 feature “Thorough testing using Django test”?

How are you going to test your site, by which methods? 

Who is responsible for what in your testing? 

1. Unit Testing: unit testing tasks will carry out during the development cycle.
2. Integration Testing: after each app was implemented, phased integration testing would be conducted.
3. Deployment Testing: after integration testing, there would be a phased deployment testing.

The testing tasks will be carried out by each member of our group with respect to different app in this project.


## Project timetable and division of work
Initial timetable for the design and implementation of features and +2 features
- Which group member(s) will be responsible for what feature
How much time each group member promises to course project per week, or better yet, per day
- Note down each members promise for committed hours for this project.
Who and when will create the GitLab issues and assign them

As each member in our group takes responsible for different apps in this project, so all of the features before-mentioned will be implemented by all of our three members with respect to each app.

No. | Task Name | Features | Developer | Start | End 
--- | --------- | -------- | --------- | ----- | --- 
1|Project Startup| |Huang Xie, Yan Feng, Liang Fang|2018/10/29|2018/10/29
2|Mandatory Features Analysis| |Huang Xie, Yan Feng, Liang Fang|2018/10/29|2018/10/29
3|+2 Features Analysis| |Huang Xie, Yan Feng, Liang Fang|2018/10/29|2018/10/29
4|Development Convention| |Huang Xie, Yan Feng, Liang Fang|2018/10/29|2018/10/29
-|Using Virtual Environment|Mandatory| |2018/10/29|2018/10/29
-|Web Development Validation|Mandatory| |2018/10/29|2018/10/29
-|GitLab's Issue Board|Mandatory| |2018/10/29|2018/10/29
-|GitLab Commits|Mandatory| |2018/10/29|2018/10/29
-|Project Progress|Mandatory| |2018/10/29|2018/10/29
-|Deployment on Heroku|Mandatory| |2018/10/29|2018/10/29
5|Deployment of Demo App on Heroku| |Huang Xie|2018/10/29|2018/10/29
6|System Design| |Huang Xie, Yan Feng, Liang Fang|2018/10/29|2018/11/03
-|Separated Django Apps Design|+1| |2018/10/29|2018/11/03
-|Bootstrap for mobile|+2| |2018/10/29|2018/11/03
-|Using PostgreSQL|+2| |2018/10/29|2018/11/03
7|System Implementation & Unit Testing| | |2018/11/04|2018/11/28
-|Users App| |Huang Xie|2018/11/04|2018/11/28
-| -- Functional Implementation|Mandatory| |2018/11/04|2018/11/28
-| -- User Searchable|+1| |2018/11/04|2018/11/28
-| -- Email Validation on Sign-Up|+1| |2018/11/04|2018/11/28
-| -- Password Reset|+1| |2018/11/04|2018/11/28
-| -- Unit Testing using Django Test|+3| |2018/11/04|2018/11/28
-|Profiles App| |Huang Xie|2018/11/04|2018/11/28
-| -- Functional Implementation|Mandatory| |2018/11/04|2018/11/28
-| -- Unit Testing using Django Test|+3| |2018/11/04|2018/11/28
-|Friendships App| |Yan Feng|2018/11/04|2018/11/28
-| -- Functional Implementation|Mandatory| |2018/11/04|2018/11/28
-| -- Unit Testing using Django Test|+3| |2018/11/04|2018/11/28
-|Discussions App| |Yan Feng|2018/11/04|2018/11/28
-| -- Functional Implementation|Mandatory| |2018/11/04|2018/11/28
-| -- Discussions Searchable|+1| |2018/11/04|2018/11/28
-| -- Unit Testing using Django Test|+3| |2018/11/04|2018/11/28
-|Events App| |Liang Fang|2018/11/04|2018/11/28
-| -- Functional Implementation|Mandatory| |2018/11/04|2018/11/28
-| -- Events Searchable|+1| |2018/11/04|2018/11/28
-| -- Unit Testing using Django Test|+3| |2018/11/04|2018/11/28
-|Groups App| |Liang Fang|2018/11/04|2018/11/28
-| -- Functional Implementation|Mandatory| |2018/11/04|2018/11/28
-| -- Unit Testing using Django Test|+3| |2018/11/04|2018/11/28
8|Mid-Project Check-in| |Huang Xie, Yan Feng, Liang Fang|2018/11/21|2018/11/21
9|Integration Testing| |Huang Xie, Yan Feng, Liang Fang|2018/11/29|2018/12/04
10|Deployment Testing| |Huang Xie, Yan Feng, Liang Fang|2018/12/05|2018/12/08
11|Final Project Documents| |Huang Xie, Yan Feng, Liang Fang|2018/12/05|2018/12/08