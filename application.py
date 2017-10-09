import logging
import logging.handlers

from wsgiref.simple_server import make_server


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/opt/python/log/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

signin = """
<link
href="https://fonts.googleapis.com/css?family=Open+Sans:300,400&emsp;Raleway&emsp;Roboto:300,400,700&emsp;Heebo:300" rel="stylesheet">


<script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.js"></script>


<link rel="stylesheet" media = "screen"
href="https://fontlibrary.org/face/glacial-indifference" type = "text/css">

<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>

<style>
    body {
        font-family: 'Segoe UI';
        font-size: 16px; 

        font-weight:300;
    }

    input {
        width:30px;

        border-style:none;

    }

    .h1 {
        font-size: 80px; 
    }

    .h2 {
        font-size:40px;
    }

    .h3 {
        font-size:20px;
    }

    .fixed {
        position:fixed;
    }

    .message {
        line-height: 20px;
        text-align: left;

        font-size:14px;

        word-wrap: break-word;

        max-width: 500px;

        display:inline-block;

        margin-bottom: 2px;
        margin-left: 10px;

        background: #44BEC7; /*0084FF*/
        border:0;
        border-radius:20px;

        font-weight:400;
        color: white;

        padding:6px 12px 6px 12px;
    }

    .message-name {
        font-size:11px;
        margin-left: 22px;

        color:gray;
    }

     ::-webkit-scrollbar
{
  width: 12px;  /* for vertical scrollbars */
  height: 12px; /* for horizontal scrollbars */
}

::-webkit-scrollbar-track
{
  background: rgba(0, 0, 0, 0.1);
}

::-webkit-scrollbar-thumb
{
  background: rgba(0, 0, 0, 0.5);
}
</style>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

  <meta name="google-site-verification" content="gGhQ7WfMBzR7vcveQLa0TU0hI5O75E7XEUE59Hf1CWQ" />

  <title>Knight Chat</title>
</head>

<html>
    <body style = 'background-color:skyblue'>
        <div style = 'width:100%; height:100%;position:absolute; top:0; left:0' class = 'valign-wrapper page'>
            <div style = 'margin-left:50px;' class = ''>
                    <input id = 'p' type = 'text' spellcheck="false" value = '****' style = 'width:80%; height:150px; font-size:80; border-style:none'><i id = 'submit-p' class = 'medium material-icons'>arrow_forward</i>
            </div>
        </div>
    </body>
</html>
"""

welcome = """
<link
href="https://fonts.googleapis.com/css?family=Open+Sans:300,400&emsp;Raleway&emsp;Roboto:300,400,700&emsp;Heebo:300" rel="stylesheet">


<script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.js"></script>


<link rel="stylesheet" media = "screen"
href="https://fontlibrary.org/face/glacial-indifference" type = "text/css">

<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/visibility.js/1.2.4/visibility.min.js"></script>

<style>
    body {
        font-family: 'Segoe UI';
        font-size: 16px; 

        font-weight:300;
    }

    .h1 {
        font-size: 80px; 
    }

    .h2 {
        font-size:40px;
    }

    .h3 {
        font-size:20px;
    }

    .fixed {
        position:fixed;
    }

    .message {
        line-height: 20px;
        text-align: left;

        font-size:14px;

        word-wrap: break-word;

        max-width: 500px;

        display:inline-block;

        margin-bottom: 2px;
        margin-left: 10px;

        background: #44BEC7; /*0084FF*/
        border:0;
        border-radius:20px;

        font-weight:400;
        color: white;

        padding:6px 12px 6px 12px;
    }

    .message-name {
        font-size:11px;
        margin-left: 22px;

        color:gray;
    }

     ::-webkit-scrollbar
{
  width: 12px;  /* for vertical scrollbars */
  height: 12px; /* for horizontal scrollbars */
}

::-webkit-scrollbar-track
{
  background: rgba(0, 0, 0, 0.1);
}

::-webkit-scrollbar-thumb
{
  background: rgba(0, 0, 0, 0.5);
}

.page {
    -webkit-transition: all 1s ease;
    -moz-transitition: all 1s ease;
    -o-transition: all 1s ease;
    transition: all 1s ease;
        
    background-color:skyblue;

}
</style>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

  <meta name="google-site-verification" content="gGhQ7WfMBzR7vcveQLa0TU0hI5O75E7XEUE59Hf1CWQ" />

  <title>Google</title>
</head>

<html>
    <body style = 'background-color:#009688; overflow-x:hidden'>
        <div style = 'width:100%; height:100%;position:absolute; top:0; left:0; background-color:#009688' class = 'valign-wrapper page'>
            <div style = 'margin-left:50px;' class = ''>
                    <div class = 'h1' style = ''></div>

                    <input id = 'password' type = 'password' spellcheck="false" placeholder= 'password' style = 'width:80%; height:150px; font-size:80; border-style:none'><i id = 'submit-password' class = 'medium material-icons'>arrow_forward</i>
            </div>
        </div>

        <div style = 'width:100%; height:100%;position:absolute; top:0; left:100%; background-color:#e57373' class = 'valign-wrapper page'>
            <div style = 'margin-left:50px;' class = ''>
                    <div class = 'h1' style = ''>Handle</div>

                    <input id = 'handle' type = 'text' spellcheck="false" placeholder= 'Type a user name' style = 'width:80%; height:150px; font-size:80; border-style:none'><i id = 'submit-handle' class = 'medium material-icons'>arrow_forward</i>
                    <div id = 'error' class = 'h3' style = 'width:80%; color: #c62828'></div>

                    <div class = 'h3' style = 'width:80%'>Enter a unique username, if you're new to KnightChat, or enter a username you've used in the past to access missed server messages.</div>
            </div>
        </div>
        
        <div style = 'width:100%; height:100%;position:absolute; top:0; left:200%; background-color:#df972d' class = 'valign-wrapper page'>
            <div style = 'margin-left:50px;' class = ''>
                    <div class = 'h1' style = ''>Server</div>

                    <input id = 'server' type = 'text' placeholder= 'Type a server name' spellcheck="false" style = 'width:80%; height:150px; font-size:80; border-style:none'><i id = 'submit-server' class = 'medium material-icons'>arrow_forward</i>
                    
                    <div id = 'server-error' class = 'h3' style = 'width:80%; color: #c62828'></div>

                    <div class = 'h3' style = 'width:80%'>Enter a server name, or pick one that you've joined before in the list below. If a friend has already entered a server, you can type in the same name to join his server. To create your own, enter a unique server name</div>

                    <div id = 'servers-joined-before' class = 'h3' style = 'width:80%'>Servers you've joined before: </div>
            </div>
        </div>

        <div style = 'width:100%; height:100%;position:absolute; top:0; left:300%; background-color:#41b6ff' class = 'page'>
            <div style = 'margin-left:50px;' class = ''>
                    <div class = 'h1' style = '' id = 'server-name'>Message</div>

                    <div style = 'background : rgba(255, 255, 255, .8); width: 100%; max-width: 650px; height: calc(90% - 70px); border-radius: 30px; margin-top:20px; padding-top: 5px; margin-bottom:-10px; position:relative'>
                        <div style = 'height:calc(100% - 110px);font-family: "Segoe UI";width:100%;overflow:auto;margin-top:10px; padding:0 10 10 0; position:relative' id = 'message-display'>
                            <div id = 'seen-indicator' style = 'font-weight:500;width:100%; text-align:right; margin-right:12px; font-size:11px'></div>
                        </div>

                        <div id = 'emojis' style = 'display:none; overflow-y:scroll; overflow-x:hidden; position:absolute; padding-bottom:10px; bottom:110px; left:0; border-radius:30px; height:100px; width:100%; background-color:rgba(255, 255, 255, .7)'></div>

                        <div id = 'message' contentEditable="true" rows="4" cols="80" data-text="Type a message" onkeypress = "send(event, this)" style = 'height:100px; width:calc(100% - 50px); font-weight:500; background-color:rgba(255, 255, 255, 0); color:black; overflow-y:auto; overflow-x:hidden; font-family:"Segoe UI"; border-radius:20px; border:0; padding:0px 0px 5px 15px; outline:none;margin-top:0px; display:inline-block; position:absolute; bottom:5px";'></div>

                        <i id = 'show-emojis' class = 'small material-icons' style = 'position:absolute; right: 10px; bottom:70px;'>tag_faces</i>
                    </div>
            </div>
        </div>
    </body>

    <script>

        var handle;
        var server;

        var prev_message;

        var page = 0;
        function shift_forward(){
            page ++;
            var c = document.getElementsByClassName("page");

            for (i = 0; i < c.length; i++){
                c[i].style['left'] = -100 * page + i * 100 + '%';
            }
        }

        var face_emojis ='https://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/grinning-face_1f600.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/grinning-face-with-smiling-eyes_1f601.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-tears-of-joy_1f602.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-open-mouth_1f603.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-open-mouth-and-smiling-eyes_1f604.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-open-mouth-and-cold-sweat_1f605.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-open-mouth-and-tightly-closed-eyes_1f606.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/winking-face_1f609.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-smiling-eyes_1f60a.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-savouring-delicious-food_1f60b.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-sunglasses_1f60e.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-heart-shaped-eyes_1f60d.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-throwing-a-kiss_1f618.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/kissing-face_1f617.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/kissing-face-with-smiling-eyes_1f619.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/kissing-face-with-closed-eyes_1f61a.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/white-smiling-face_263a.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/slightly-smiling-face_1f642.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/neutral-face_1f610.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/expressionless-face_1f611.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-without-mouth_1f636.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smirking-face_1f60f.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/persevering-face_1f623.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/disappointed-but-relieved-face_1f625.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-open-mouth_1f62e.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/hushed-face_1f62f.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/sleepy-face_1f62a.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/tired-face_1f62b.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/sleeping-face_1f634.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/relieved-face_1f60c.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-stuck-out-tongue_1f61b.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-stuck-out-tongue-and-winking-eye_1f61c.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-stuck-out-tongue-and-tightly-closed-eyes_1f61d.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/unamused-face_1f612.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-cold-sweat_1f613.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/pensive-face_1f614.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/confused-face_1f615.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/astonished-face_1f632.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/confounded-face_1f616.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/disappointed-face_1f61e.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/worried-face_1f61f.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-look-of-triumph_1f624.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/crying-face_1f622.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/loudly-crying-face_1f62d.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/frowning-face-with-open-mouth_1f626.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/anguished-face_1f627.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/fearful-face_1f628.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/weary-face_1f629.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/grimacing-face_1f62c.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-open-mouth-and-cold-sweat_1f630.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-screaming-in-fear_1f631.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/flushed-face_1f633.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/dizzy-face_1f635.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/pouting-face_1f621.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/angry-face_1f620.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/face-with-medical-mask_1f637.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-halo_1f607.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/smiling-face-with-horns_1f608.pnghttps://emojipedia-us.s3.amazonaws.com/thumbs/72/facebook/65/imp_1f47f.png';
        
        face_emojis = face_emojis.split('https:');

        for (i = 1; i < face_emojis.length; i++){
            var emoji_url = 'https:' + face_emojis[i];
            var emoji = document.createElement("IMG");
            emoji.src = emoji_url;

            emoji.style['width'] = '30px';
            emoji.style['height'] = '30px';

            emoji.style['margin-left'] = '10px';
            emoji.style['margin-right'] = '10px';
            emoji.style['margin-top'] = '10px';

            emoji.id = 'emoji-' + i;

            document.getElementById('emojis').appendChild(emoji);

            $('#emoji-' + i).click(function (){
                var new_emoji = document.createElement("IMG");
                new_emoji.src = this.src;

                new_emoji.style['width'] = '20px';
                new_emoji.style['height'] = '20px';

                document.getElementById("message").appendChild(new_emoji);
                document.getElementById("message").innerHTML += ' ';
            });

        } 

        var showing_emojis = false;

        $('#show-emojis').click(function () {
            if (!showing_emojis){
                $('#emojis').css('display', 'inline');
                showing_emojis = true;
            }else{
                $('#emojis').css('display', 'none');
                showing_emojis = false;
            }
        });


        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState === 4) {
                if (request.status === 200) {
                    
                    document.body.className = 'ok';
                    console.log(request.responseText);

                    var valid = request.responseText.split('|')[0];
                    var servers = request.responseText.split('|').slice(1).join('|').split(',');

                    var servers_string = "";
                    for (i = 0; i < servers.length; i++){
                        if (i != servers.length - 1){
                            servers_string += "<div id = 'server-" + i + "' class = 'chip' style = ''>" + servers[i] + "</div> ";
                        }else{
                            servers_string += "<div id = 'server-" + i + "' class = 'chip' style = ''>" + servers[i] + "</div> ";
                        }
                    }

                    servers_string = "Servers you've joined before: " + servers_string;

                    document.getElementById("servers-joined-before").innerHTML = servers_string;

                    for (i = 0; i < servers.length; i++){
                        $('#server-' + i).click(function() {
                            console.log($(this).text());
                            $('#server').val($(this).text());
                        });
                    }

                    if (valid === "OK"){
                        shift_forward();
                    }else{
                        document.getElementById("error").innerHTML = request.responseText.split('|')[1];
                    }
                } else {
                    document.body.className = 'error';
                }
            }
        };

        var missed_messages = 0;

        var message_request = new XMLHttpRequest();
        message_request.onreadystatechange = function() {
            if (message_request.readyState === 4) {
                if (message_request.status === 200) {
                    document.body.className = 'ok';
                    console.log(message_request.responseText);

                    var message_name = document.createElement("DIV");
                    var new_message = document.createElement("DIV");


                    var M = message_request.responseText.split(':');

                    if (M[1] === " servername accepted"){
                        shift_forward();

                        // start a new request
                        message_request.open("POST", "http://knightchat.newportrocketry.com/", true);
                        message_request.send("REQUEST_LAST_10:" + handle + ',' + server);
                        return;
                    }else if (M[0] === "FAILED"){
                        document.getElementById("server-error").innerHTML = M[1];
                        return;
                    }else if (M[1] === "MISSEDNOTHING"){
                        console.log("RESETING REQUEST FOR MESSAGE");

                        message_request.open("POST", "http://knightchat.newportrocketry.com/", true);
                        message_request.send("WHAT_HAVE_I_MISSED:" + handle + ',' + server);
                        return;
                    }

                    new_message.innerHTML = M.slice(1).join(':').split('|')[1].slice(0, -1);

                    message_name.innerHTML = M[1].split('|')[0];
                    message_name.classList.add("message-name");

                    new_message.classList.add("message");

                    var message_ = M.slice(1).join(':').split('|')[1];

                    if (M[1].split('|')[1] != ''){
                        
                        missed_messages ++;
                        document.title = '(' + missed_messages + ') Google';

                        if (M[1].split('|')[0] != ' ' + handle){
                            var wrapper = document.createElement("DIV");
                            wrapper.style['width'] = '100%';
                            wrapper.style['text-align'] = 'right';

                            if (message_.slice(-1) == '^' || prev_message == undefined){
                                message_name.style['margin-right']= '12px';
                                wrapper.appendChild(message_name);
                                
                                document.getElementById("seen-indicator").innerHTML = '';


                            }else if (message_.slice(-1) == '*'){
                                prev_message.style['border-bottom-right-radius'] = '4px';
                                new_message.style['border-top-right-radius'] = '4px';  

                                document.getElementById("seen-indicator").innerHTML = '';

                            }else if (message_.slice(-1) == '%'){
                                new_message.innerHTML = "";

                                if (document.getElementById("seen-indicator").innerHTML === ""){
                                    document.getElementById("seen-indicator").innerHTML += "Seen by " + M[1].split('|')[0];
                                }else{
                                    document.getElementById("seen-indicator").innerHTML += ',' + M[1].split('|')[0];
                                }
                                
                                missed_messages --;
                            }

                            if (message_.slice(-1) != '%'){
                                wrapper.appendChild(new_message);

                                prev_message = new_message;
                                new_message.style['background-color'] = '#13CF13';

                                document.getElementById('message-display').insertBefore(wrapper, document.getElementById("seen-indicator"));
                            }
                            
                        }else{
                            if (message_.slice(-1) == '^' || prev_message == undefined){
                                document.getElementById("message-display").insertBefore(message_name, document.getElementById("seen-indicator"));

                                document.getElementById("seen-indicator").innerHTML = '';

                            }else if (message_.slice(-1) == '*'){
                                prev_message.style['border-bottom-left-radius'] = '4px';
                                new_message.style['border-top-left-radius'] = '4px';  

                                document.getElementById("seen-indicator").innerHTML = '';
 
                            }else if (message_.slice(-1) == '%'){
                                new_message.innerHTML = "";
                                
                                if (document.getElementById("seen-indicator").innerHTML === ""){
                                    document.getElementById("seen-indicator").innerHTML += "Seen by " + M[1].split('|')[0];
                                }else{
                                    document.getElementById("seen-indicator").innerHTML += ',' + M[1].split('|')[0];
                                }

                                missed_messages --;

                            }

                            

                            if (message_.slice(-1) != '%'){
                                prev_message = new_message;
                                new_message.style['background-color'] = '#0084FF';

                                document.getElementById('message-display').insertBefore(new_message, document.getElementById("seen-indicator"));
                                document.getElementById('message-display').insertBefore(document.createElement("BR"), document.getElementById("seen-indicator"));
                            }
                        }

                        document.getElementById("message-display").scrollTop = document.getElementById("message-display").scrollHeight;
                    }


                    // start a new request
                    message_request.open("POST", "http://knightchat.newportrocketry.com/", true);
                    message_request.send("WHAT_HAVE_I_MISSED:" + handle + ',' + server);

                } else {
                    document.body.className = 'error';
                }
            }
        };



        $('#submit-handle').click(function() {
            request.open("POST", 'http://knightchat.newportrocketry.com/', true);
            request.send("USER_HANDLE:" + $('#handle').val());

            handle = $('#handle').val();
            console.log("post");
        }); 

        $('#submit-server').click(function() {
            console.log("submitting servername");
            message_request.open("POST", 'http://knightchat.newportrocketry.com/', true);
            message_request.send("USER_JOIN_SERVER:" + handle + ',' + $('#server').val());
        
            server = $('#server').val();
            console.log(server);
            $('#server-name').html(server);
            
        });

        $('#submit-update').click(function() {
            request.open("POST", 'http://knightchat.newportrocketry.com/', true);
            request.send("USER_MESSAGE:" + handle + ',' + server + ',' + $('#message').val());

            $('#message').val('');

        });

        $('#submit-password').click(function() {
            if ($('#password').val() == '271828'){
                shift_forward();
            }
        })

        function send(e, textarea){
            var code = (e.keyCode ? e.keyCode : e.which);
            if (code == 13){
                e.preventDefault();
                
                request.open("POST", 'http://knightchat.newportrocketry.com/', true);
                request.send("USER_MESSAGE:" + handle + ',' + server + ',' + $('#message').html());

                $('#message').text('');
                document.getElementById("message").innerHTML = "";
            }
        }

        Visibility.every(1000, function () {
            if (missed_messages != 0){
                missed_messages = 0;        // reset

                request.open("POST", 'http://knightchat.newportrocketry.com/', true);
                request.send("USER_MESSAGE_SEEN:" + handle + ',' + server);
            }
        });

    </script>
</html>
"""

import time 

servers = {}
server_log = {}

messages = []

def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':

                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size).decode()
                logger.info("Received message: %s" % request_body)
                
                status = '200 OK'
                headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]
                
                start_response(status, headers)

                messages.append(request_body)

                request_bodies = request_body.split(':')
                main_body = ':'.join(request_bodies[1:])
                query = request_bodies[0]

                if query == 'USER_HANDLE':
                    # Check all servers the user has joined before
                    servers_joined = ""
                    for s in servers:
                        if main_body in servers[s]:
                            servers_joined += s + ','

                    if set(main_body).intersection(set('`~!@#$%^&*()_+-=[]{}\\|\'\";:/?.>,<')):
                        # Sequential decryption, every pass gives the next code encryption

                        return ["FAILED|No special characters allowed, letters a-z + A-Z, numbers and spaces only"]

                    return ["OK|" + servers_joined[:-1]]
            
                elif query == 'USER_JOIN_SERVER':
                    # todo, check username for validity 

                    # Input should be username,servername
                    parameters = main_body.split(',')

                    if set(parameters[1]).intersection(set('`~!@#$%^&*()_+-=[]{}\\|\'\";:/?.>,<')):
                        # Sequential decryption, every pass gives the next code encryption

                        return ["FAILED:No special characters allowed, letters a-z + A-Z, numbers and spaces only"]

                    if parameters[1] not in servers:
                        servers[parameters[1]] = {parameters[0]:[], "last":""}
                        server_log[parameters[1]] = []
                    else:
                        if parameters[0] not in servers[parameters[1]]:
                            servers[parameters[1]][parameters[0]] = []

                    return ["Server: servername accepted"]
            
                elif query == "WHAT_HAVE_I_MISSED":
                    # Input should be username,servername
                    parameters = main_body.split(',')

                    cycles = 0
                    while (not servers[parameters[1]][parameters[0]]):
                        cycles += 1
                        time.sleep(0.2)

                        if (cycles >= 300):
                            return [parameters[0] + ":MISSEDNOTHING"]

                        pass 

                    o = [parameters[0] + " has requested the information it has missed: " + servers[parameters[1]][parameters[0]][0]]
                   
                        
                    del servers[parameters[1]][parameters[0]][0]
                    
                    return o
            
                elif query == "USER_MESSAGE_SEEN":
                    parameters = main_body.split(',')

                    s = servers[parameters[1]]

                    for k in s:
                        if k != "last" and k != "name":
                            s[k].append(parameters[0] + '|' + '%');

                elif query == "USER_MESSAGE":
                    # Input should be username,servername,message
                    parameters = main_body.split(',')

                    message = ','.join(parameters[2:])

                    s = servers[parameters[1]]
                    
                    if s['last'] == parameters[0]:
                        # REAL IMPORTANT, KEEP THIS LIST LIMITED
                        server_log[parameters[1]].append(parameters[0] + '|' + message + '*')
                    else:
                        server_log[parameters[1]].append(parameters[0] + '|' + message + '^')

                    for k in s:
                        if k != "last" and k != "name":
                            if s['last'] == parameters[0]:

                                # REAL IMPORTANT, KEEP THIS LIST LIMITED

                                s[k].append(parameters[0] + '|' + message + '*')
                            else:

                                s[k].append(parameters[0] + '|' + message + '^')
                                
                    
                    s['last'] = parameters[0]
                
                elif query == "REQUEST_LAST_10":
                    # request last ten messages from log
                    parameters = main_body.split(',')
                    # input should be username,servername

                    servers[parameters[1]][parameters[0]] = server_log[parameters[1]][-10:]
                    return parameters[0] + ':MISSEDNOTHING'

                return [request_body]
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    status = '200 OK'
    headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]

    start_response(status, headers)
    return [response]


if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
