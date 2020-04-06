# AstrometricsPy

This repo is inspired in [Astrometrics](https://github.com/quintoandar/astrometrics) and it is intended to provide 
a hands-on workshop like in the Astronometrics Wiki page.
  
It has the following endpoints:

1. Find the meaning of some word (in english):
    * `http://localhost:8080/words/meaning/<some-word>`

2. Try to match two words based on [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) (in english):
    * `https://localhost:8080/words/match/<word1>/<word2>`

### Aims

1 - Create Prometheus Metrics App

2 - How to instrument Flask App

3 - Provide App tracing

### TODOs

- [ ] Organize metrics inside endpoints and not in `__init__.py`
- [ ] Create Grafana Dashboards Counting Words, HTTP Requests, Endpoints
- [ ] Configure Prometheus volumes
- [ ] Tracing
    - [ ] [OpenTracing](https://github.com/opentracing/opentracing-python)

