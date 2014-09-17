// Javascript function to obfuscate the html that generates mailto links

function gen_mail_to_link(lhs, rhs, subject) {
    document.write("<a href=\"mailto");
    document.write(":" + lhs + "@");
    if (subject.length > 0) {
        document.write(rhs + "?subject=" + subject + "\">" + lhs + "@" + rhs + "<\/a>");
    }
    else {
        document.write(rhs + "\">" + lhs + "@" + rhs + "<\/a>");
    }
}
