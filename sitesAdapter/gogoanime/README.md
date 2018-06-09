# unofficial Gogo Anime Download API
A GogoAnime API used for downloading anime
# Requirements
BS4<br/>
Urllib
# How to use
step1. Import the module
```python 
import GogoAPI as gogo
```
<br/>

step2. search the anime 
```pyhton
results = gogo.searchResults("steins;Gate")
```
(steins;gate is an example)<br/>

step3. print results (optional)
```python
for links in results:
  print(links.title)
  ```
<br/>

step4. pick the show you want to download(you must specify the episode)
```python
print(gogo.getDLLink(results[0].link+"5"))
```
(result 0 and episode 5 are examples)

# Final notes
Feel free to ask for any help or if you have suggestions

