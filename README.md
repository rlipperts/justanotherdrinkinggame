# Modern drinking game written by ~~actual computer scientist~~ arrogant idiots

![Mindmap](doc/img/mindmap.png "Quick brainstorming")

## Ideas
 
### Feedback
* Users can up- and downvote games, data sets or a single datum
* Users can suggest new data

### Statistics
* Gather data of how much which player had to drink
* Give out Awards and achievements
* User database to gather statistics and show off how big of an alcohol addict you are

## Concepts

### Game Factory
_Factory that creates game instances from Configurations_
* 

### Services
_Different services to dispatch by the game factory (service factory)_
* 

#### Timer
_Frequently sends Timer events to the Game connected to it_
* 

### Games
_Different drinking games that you can play_
* Basically, they are defined by their interface and their internal functionality that converts input into output

#### Interface
* __Configuration__: Information required to set up a game session
* __Input__: Triggers of game action
* __Output__: Information on what player needs to do what

#### Active/Passive Games
* Passive games do not require user input after configuration
    * The Game just outputs e.g. actions to perform in a certain frequency
    * Game output is not triggered by human-initiated events
* Active games require user-interaction and -attention
    * The game sends requests and actions and responds to the user input
    * Game output is triggered by all types of events (including user input)

### Event
* Interface to trigger game actions
* Example events:
    * Timers
    * Other bots contacting this game service (Goals during sport events, social media posts, ...)
    * User input from a frontend
   
## Games

### Do-This
_Sends out actions to perform by certain users_
* __Configuration:__ List of users, Action data lists
* __Input:__ Timerevent (also just a bit)
* __Output:__ User, Action
* Action data is selected from a number of existing datasets
    * Separate module maintains those
    
### Roll-and-Drink
_Allows users to request a random number of sips to take_
* __Configuration:__ None
* __Input:__ Request (basically just a bit)
* __Output:__ Number of Sips
* Simple proof-of-concept game for those that do not play games for fun (I'm looking at you, fellow League of Legend players!)