# clockify
For CS448B -- tracking music habits over time

https://ezeada.github.io/clockify/

## Motivation
I created this tool because I listen to a lot of music (about 6 and a half hours a day). The type of music I listen to varies depending on what I'm doing, so when I'm studying (probably in the early afternoon and evening), I know from experience that I'm listening to music with a lower tempo and less lyrics, for example. I wanted to create a tool that could provide a concrete visualization for the music-listening habits I think I've acquired, and do the same for those that listen to music as frequently as I do. My sample dataset is replicated Spotify data from Jan 29th of to Feb 28th of this year. Each entry contains the artist, album, track, date, time, and corresponding Spotify features for the song. For demo purposes, the tool is already loaded with the sample dataset. 

## Instructions

### View
With the dropdown at the top, you can switch to month view (which averages the values for each day), or back to day view (which averages the values for each hour of the day). 

### Choosing Features, Colors, and Other Visual Adjustments 
The first feature in the left sidebar allows you to choose which features to focus on. 
The next two are purely up to personal preference. The default stroke color is set to None because it makes it easier to compare color for me, but if colors are too similar, using a black or white stroke may help differentiate between segments. The Inner Radius slider is self-explanatory.
Under visualization colors, there is a key that provides a rough estimate of colors and and their corresponding percentile values. However, if you want to see exact values, you can hover over a segment and look at its tooltip under "Scaled Value".

You can adjust the color of the visualization by clicking on the key and selecting from the color picker. *Please note that hours or days without any entries (during when no music was listened to) will show up as black.

### Adjusting the Percentile Range
A lot of values will probably fall into the midrange (around the 50th) percentile. This makes sense, especially considering that they’re averages. If you want to see more contrast, or the values don't vary as much as you'd like, you can clip the minimum and maximum percentile values using the "Percentile Range" slider. (The key will change accordingly.) Note that segments with scaled values that fall below your minimum value or above your maximum value will automatically scale their color with white as 0th percentile and 100th percentile, respectively.

### Search and Top Artists/ Songs
When you click on each segment, you can get the top artists and songs of that segment time period in the bottom right hand corner, to grasp what artists and songs may contribute to what percentiles for each measure. 

If you'd like to search a specific song from below to see its stats, you can do so and get all of the corresponding percentiles for that specific song, as well as how often you listened to it and what hour on average. 
