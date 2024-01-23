css = '''
<style>

[ data-testid="stAppViewContainer"] {
    
background-image: url("https://images.pexels.com/photos/5208362/pexels-photo-5208362.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");

background-size: cover;

}

.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    align-items: center; 
}

.chat-message.user {
    background-color: #2b313e
}

.chat-message.bot {
    background-color: #475063
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/R30gsMV/robot.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/37RZbFv/human.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''