# clockify
For CS448B -- tracking music habits over time

https://ezeada.github.io/clockify/

I created this tool because I listen to a lot of music--if we assume the average song is about 3 minutes--then this translates to about 6 and a half hours of music a day. The type of music I listen to varies depending on what I'm doing, so when I'm studying (probably in the early afternoon and evening), I know from experience that I'm listening to music with a lower tempo and less lyrics, for example. I wanted to create a tool that could provide a concrete visualization for the music-listening habits I think I've acquired, and do the same for those that listen to music as frequently as I do.

My sample dataset is replicated Spotify data from Jan 29th of to Feb 28th of this year. Each entry contains the Artist, album, track, date, time, and corresponding Spotify features for the song.

Here is the tool already loaded with my sample dataset. With the dropdown at the top, we can switch to month view (which averages the values for each day), or back to day view (which averages the values for each hour of the day). 

The first feature in the left sidebar allows you to choose which features to focus on. Say, I only really cared about how tempo varies throughout the day, or my other features are pretty similar across hours. Now, I can focus on only tempo. 

The next two are purely up to personal preference. The default stroke color is set to None because it makes it easier to compare color for me, but if colors are too similar, using a black or white stroke may help differentiate between segments. 

The Inner Radius slider is self-explanatory.

Under visualization colors, there is a key that provides a rough estimate of colors and and their corresponding percentile values. However, if you want to see exact values, you can hover over a segment and look at its tooltip under "Scaled Value".

You can adjust the color of the visualization by clicking on the key and selecting from the color picker. However, please note that hours or days without any entries (during when no music was listened to) will show up as black.

Although I can pick out standout segments from my visualization, a lot of values fall into this midrange 50th percentile. This makes sense, especially considering that they’re averages. If I want to see more contrast, or the values don't vary as much as I'd hoped, I can clip the minimum and maximum percentile values using the "Percentile Range" slider. The key will change accordingly. Now, the yellowish color corresponds to the 25th percentile and the blue corresponds to the 80% percentile. Note that segments that fall below your minimum value will automatically scale their color with white as 0th percentile .

When you click on each segment, you can get the top artists and songs of that segment time period in the bottom right hand corner, to grasp what artists and songs may contribute to what percentiles for each measure. 

If you'd like to search a specific song from below to see its stats, you can do so and get all of the corresponding percentiles for that specific song, as well as how often you listened to it and what hour on average. 
