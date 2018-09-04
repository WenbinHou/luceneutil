#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import competition

# simple example that runs benchmark with WIKI_MEDIUM source and taks files 
# Baseline here is ../lucene-solr versus ../patch
if __name__ == '__main__':
  sourceData = competition.sourceData()
  comp = competition.Competition(
    randomSeed = 0xdeadbeef,
    jvmCount = 5,  # num of iter
    taskRepeatCount = 32)  # repeat task in every iter


  #index = comp.newIndex('lucene-solr-6.6.5', sourceData)
  index = comp.newIndex('lucene-solr-6.6.5', sourceData,
                        facets = (('taxonomy:Date', 'Date'),
                                  ('taxonomy:Month', 'Month'),
                                  ('taxonomy:DayOfYear', 'DayOfYear'),
                                  ('sortedset:Month', 'Month'),
                                  ('sortedset:DayOfYear', 'DayOfYear'))) #,
                        # Added by Wenbin
                        #directory="MMapDirectory",  # default: MMapDirectory
                        #maxConcurrentMerges=3,  # use 1 for spinning-magnets and 3 for fast SSD
                        #optimize=True)


  # create a competitor named baseline with sources in the ../lucene-solr-6.6.5 folder
  comp.competitor('6.6.5', 'lucene-solr-6.6.5',
                  index = index)

  # use the same index here
  # create a competitor named my_modified_version with sources in the ../lucene-solr-6.6.5 folder
  # note that we haven't specified an index here, luceneutil will automatically use the index from the base competitor for searching 
  # while the codec that is used for running this competitor is taken from this competitor.
  comp.competitor('6.6.5', 'lucene-solr-6.6.5',
                  index = index)

  # start the benchmark - this can take long depending on your index and machines
  comp.benchmark("lucene_6.6.5")

