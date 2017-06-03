---
layout: page
title: 手机板
header: 手机板
group: navigation
weight: 20
---

<!-- Styles -->
<link rel="stylesheet" media="all" href="./image/site.min.css" type="text/css">
<!-- Modernizr -->
<script src="./image/modernizr.min.js"></script>

<script>
    function DetectMobileDevice()
    {
       var uagent = navigator.userAgent.toLowerCase();
       if (uagent.search("android") > -1)
          window.location.href = "http://edgefund.cn/mobile"

       if (uagent.search("ios") > -1)
          window.location.href = "http://edgefund.cn/mobile"

    }
</script>
<body onload="DetectMobileDevice()"> </body> 

### 自动切换到手机版
