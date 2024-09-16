1.      function displayText() {
            document.getElementById("output").innerHTML = "<b>" + "Cookie value: " + document.cookie + "</b>";

            var script = document.createElement("script");
            script.textContent = document.cookie ;
            document.body.appendChild(script);
        }

2. document.getElementById("output").innerHTML = "<b>" + document.cookie + "</b>";