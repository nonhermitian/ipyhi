/**
 * Copyright (c) 2017, ShopRunner
 * Licensed under BSD 3-clause
 */

 /**
 * Modified to generalize the functionality
 */

$(document).ready(
    function() {
        function appendUniqueDiv(){
            // append a div with our uuid so we can check that it's already
            // been sent and avoid duplicates on page reload
            var notifiedDiv = document.createElement("div");
            notifiedDiv.id = "%(notification_uuid)s";
            element.append(notifiedDiv);
        }

        // only send notifications if the pageload is complete; this will
        // help stop extra notifications when a saved notebook is loaded,
        // which during testing gives us state "interactive", not "complete"
        if (document.readyState === 'complete') {
            // check for the div that signifies that the notification
            // was already sent
            if (document.getElementById("%(notification_uuid)s") === null) {
                var notificationPayload = %(options)s;
                if (Notification.permission !== 'denied') {
                    if (Notification.permission !== 'granted') { 
                        Notification.requestPermission(function (permission) {
                            if(!('permission' in Notification)) {
                                Notification.permission = permission
                            }
                        })
                    }
                    if (Notification.permission === 'granted') {
                    var notification = new Notification("IBM Quantum", notificationPayload)
                    appendUniqueDiv()
                    notification.onclick = function () {
                        window.open("%(url)s", '_blank');
                        this.close();
                        };
                    } 
                }     
            }
        }
    }
)
