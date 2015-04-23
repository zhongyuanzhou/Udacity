# %load data.py
#!/usr/bin/env python
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}
You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB. You could also do some cleaning
before doing that, like in the previous exercise, but for this exercise you just have to
shape the structure.

In particular the following things should be done:
#- you should process only 2 types of top level tags: "node" and "way"
#- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
#    - attributes in the CREATED array should be added under a key "created"
#    - attributes for latitude and longitude should be added to a "pos" array,
#      for use in geospacial indexing. Make sure the values inside "pos" array are floats
#      and not strings.
#- if second level tag "k" value contains problematic characters, it should be ignored
#- if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
#- if second level tag "k" value does not start with "addr:", but contains ":", you can process it
  same as any other tag.
#- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:
  
<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>
  should be turned into:
{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}
- for "way" specifically:
  <nd ref="305896090"/>
  <nd ref="1719825889"/>
  
should be turned into
"node_refs": ["305896090", "1719825889"]
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
re_street = re.compile(r'^street')
re_address = re.compile(r'^addr\:')


CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    position_attributes = ['lat', 'lon']
    created_attributes = CREATED

#you should process only 2 types of top level tags: "node" and "way"
    if element.tag == "node" or element.tag == "way":
        node['type'] = element.tag
        address = {}
    
#attributes in the CREATED array should be added under a key "created"
        for key in element.attrib:
            if key in created_attributes:
                if 'created' not in node:
                    node['created'] = {}
                node['created'][key] = element.get(key) 
                
            elif key in position_attributes:
                continue
            else:
                node[key] = element.get(key)

#attributes for latitude and longitude should be added to a "pos" array,
#for use in geospacial indexing. Make sure the values inside "pos" array are floats
#and not strings.
        if 'lat' in element.attrib and 'lon' in element.attrib:
            node['pos'] = [float(element.get('lat')), 
                           float(element.get('lon'))]

#Second Level tags
        for child in element:
            if child.tag == 'nd':
                if 'node_refs' not in node:
                    node['node_refs'] = []
                if 'ref' in child.attrib:
                    node['node_refs'].append(child.get('ref'))

# throw out not-tag elements and elements without `k` or `v`
            if child.tag != 'tag'\
            or 'k' not in child.attrib\
            or 'v' not in child.attrib:
                continue
            key = child.get('k')
            value = child.get('v')

#if second level tag "k" value contains problematic characters, it should be ignored
            # skip problematic characters
            if problemchars.search(key):
                continue

#if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
# parse address k-v pairs
            elif re_address.search(key):
                key = key.replace('addr:', '')
                address[key] = value

# 
            else:
                node[key] = value
            
#address
        if len(address) > 0:
            node['address'] = {}
            full_street = None
            dict_street = {}
            format_street = ['prefix', 'name', 'type']
            
# parse through address objects

#if there is a second ":" that separates the type/direction of a street,
#the tag should be ignored
#same as any other tag.

            for key in address:
                value = address[key]
                if re_street.search(key):
                    if key == 'street':
                        full_street = value
                    elif 'street:' in key:
                        dict_street[key.replace('street:', '')] = value
                else:
                    node['address'][key] = value
# assign street_full or fallback to compile street dict
            if full_street:
                node['address']['street'] = full_street
            elif len(dict_street) > 0:
                node['address']['street'] = ' '.join([dict_street[key] for key in format_street])
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset,
    # call the process_map procedure with pretty=False. The pretty=True option adds
    # additional spaces to the output, making it significantly larger.
    data = process_map('example.osm', True)
    pprint.pprint(data)

    assert data[0] == {
                        "id": "261114295",
                        "visible": "true",
                        "type": "node",
                        "pos": [
                          41.9730791,
                          -87.6866303
                        ],
                        "created": {
                          "changeset": "11129782",
                          "user": "bbmiller",
                          "version": "7",
                          "uid": "451048",
                          "timestamp": "2012-03-28T18:31:23Z"
                        }
                      }
    print "test 1 passed."
    assert data[-1]["address"] == {
                                    "street": "West Lexington St.",
                                    "housenumber": "1412"
                                      }
    print "test 2 passed."
    assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369",
                                    "2199822370", "2199822284", "2199822281"]
    print "test 3 passed."

if __name__ == "__main__":
    test()
