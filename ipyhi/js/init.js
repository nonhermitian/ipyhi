/**
 * Copyright (c) 2017, ShopRunner
 * Licensed under BSD 3-clause
 */

 /**
 * Modified alert msg.
 */

if (!("Notification" in window)) {
    alert("This browser does not support desktop notifications, so IBM Quantum notifications will be silent.");
} else if (Notification.permission !== 'granted' && Notification.permission !== 'denied') {
    Notification.requestPermission(function (permission) {
        if(!('permission' in Notification)) {
            Notification.permission = permission;
        }
    })
}
