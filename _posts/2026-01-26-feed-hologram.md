---
title: Hologram (Interactive)
description: 
date: 2026-01-26 05:00:00 -0500
categories: [feed]
tags: [code]
pin: false
math: true
mermaid: true
pin: false
---
<div style="max-width: 900px; margin: 2rem auto;">
  <iframe
    style="width:100%; aspect-ratio:16/9; border:1px solid #222; background:black;"
    loading="lazy"
    title="Canvas visual experiment"
    srcdoc='
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: black;
    }

    header {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      padding: 8px 12px;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 14px;
      background: rgba(0, 0, 0, 0.5);
      color: #fff;
      z-index: 10;
    }

    header a {
      color: #6cf;
      text-decoration: none;
    }

    header a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

<header>
  Visual experiment by Jeff Thomas
  <a href="https://codepen.io/aecend/pen/ExWwoQL" target="_blank" rel="noopener noreferrer">
    @toshiya-marukubo
  </a>
</header>

<script>
(() => {
  "use strict";

  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");
  const diameter = 15;

  let width = 0;
  let height = 0;
  let halfWidth = 0;
  let frame;
  let time = 0;
  let destination = 1;

  const resize = () => {
    cancelAnimationFrame(frame);
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    halfWidth = width / 2;
    ctx.globalCompositeOperation = "lighter";
    loop();
  };

  const loop = () => {
    frame = requestAnimationFrame(loop);
    time += (destination - time) * 0.1;
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < height; i += diameter) {
      for (let j = 0; j < halfWidth; j += diameter) {
        for (let channel = 0; channel < 3; channel++) {
          ctx.fillStyle = ["#FF0000", "#00FF00", "#0000FF"][channel];

          const index = i * width + j;
          ctx.globalAlpha = Math.tan(index * index - time);

          ctx.fillRect(
            Math.tan(i * j - Math.sin(index + channel / 100) + time) * j + halfWidth - diameter / 2,
            i,
            Math.tan(index + i / j + time + channel / 100) / 2 * diameter / 2,
            Math.tan(index * index - time) * diameter / 2
          );
        }
      }
    }
  };

  window.onload = () => {
    ["mousemove", "touchmove"].forEach(type => {
      window.addEventListener(type, event => {
        event.preventDefault();
        const e = event.touches ? event.touches[0] : event;
        destination = e.pageX / width;
      });
    });

    canvas.style.background = "#000";
    document.body.appendChild(canvas);
    resize();
    window.onresize = resize;
  };
})();
</script>

</body>
</html>
'>
  </iframe>
</div>

