var stat_map = (function () {
    var stat_map = function (map, JSON) {

        this.loaded = false;

        this.grades = [];
        this.layer = [];
        this.map = map;
        this.info = L.control({position: 'topright'});
        this.info.that = this;
        this.legend = L.control({position: 'bottomright'});
        this.chart = L.control({position: 'bottomleft'});
        this.legend.that = this;
        this.period = 1;
        this.lineChartData = {
            labels: [],
            datasets: [
                {
                    label: "",
                    fillColor: "rgba(151,187,205,0.2)",
                    strokeColor: "rgba(151,187,205,1)",
                    pointColor: "rgba(151,187,205,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(151,187,205,1)",
                    data: []
                }
            ]
        };

        var self = this;

        this.chart.onAdd = function () {
            this._div = L.DomUtil.create('div', 'info');
            $(this._div).html('<div style="width:30em; height:15em"><div><canvas id="canvas" style="width:95%"></canvas></div></div>');
            return this._div;
        };

        this.info.onAdd = function (map) {
            var header = (self.period == 1 ? gettext("for the last 24 hours") :
                self.period == 7 ? gettext("for the last week") :
                    self.period == 31 ? gettext("for the last month") :
                        gettext("for the last year"));


            this._div = L.DomUtil.create('div', 'info');
            $(this._div).append("<h3>" + gettext("Birth registrations") + "</h3><h4>" + header + "</h4><table class='info_table'>");
            this._ul = $(this._div).find("table");
            var that = this;
            self.layer.eachLayer(
                function (layer) {
                    var class_tag = " id='info_table_" + layer._leaflet_id + "' ";
                    $(that._ul).append(
                        "<tr><td>" +
                        '<i style="background:' + self.getColor(layer.feature.properties.number) + '">&nbsp; &nbsp;</i></td>' +

                        "<td" + class_tag + ">" +

                        gettext(layer.feature.properties.NAME_1) + "</td>" +
                        "<td align='right'>" + layer.feature.properties.number + "</td>" +
                        "</tr>"
                    );


                }
            );
            return this._div;
        };

        this.legend.onAdd = function (map) {

            var div = L.DomUtil.create('div', 'info legend'), labels = [];

            for (var i = 0; i < this.that.grades.length; i++) {
                div.innerHTML +=
                    '<i style="background:' + this.that.getColor(this.that.grades[i] + 1) + '"></i> ' +
                    this.that.grades[i] + (this.that.grades[i + 1] ? ' &ndash; ' + this.that.grades[i + 1] + '<br>' : '+');
            }

            return div;
        };

        this.highlightFeature = function (e) {
            var layer = e.target;

            self.resetHighlight();

            layer.setStyle({
                weight: 3,
                color: '#666',
                dashArray: '',
                fillOpacity: 0.7
            });

            if (!L.Browser.ie && !L.Browser.opera) {
                layer.bringToFront();
            }

            $('#info_table_' + layer._leaflet_id).addClass('highlight');

            self.update_line([layer.feature.properties.ID_1]);
        };

        this.resetHighlight = function (e) {
            if (self.Line){
                self.update_line();
            }

            $('.info_table td').removeClass('highlight');

            self.layer.eachLayer(function (e) {
                self.layer.resetStyle(e);
            });

        };

    };

    stat_map.prototype.getColor = function (d) {
        if (!d) {
            return '#FFFFFF';
        }

        return d >= this.grades[8] ? '#008026' :
            d > this.grades[7] ? '#00BD26' :
                d > this.grades[6] ? '#1AE31C' :
                    d > this.grades[5] ? '#4EFC2A' :
                        d > this.grades[4] ? '#8DFD3C' :
                            d >= this.grades[3] ? '#B2FE4C' :
                                d > this.grades[2] ? '#D9FE76' :
                                    d >= this.grades[1] ? '#EDFFA0' :
                                        '#FFFFFF';
    };


    stat_map.prototype.get_stat_detail = function (ST_DV) {
        var ChartData = {};
        if (!ST_DV) {
            for (var i in this.stat_detail) {
                var point = this.stat_detail[i];
                if (ChartData[point.day]) {
                    ChartData[point.day] += point.number;
                } else {
                    ChartData[point.day] = point.number;
                }
            }
        } else {

            for (var i in this.stat_detail) {
                var point = this.stat_detail[i];
                if (point.ST_DV == ST_DV) {
                    ChartData[point.day] = point.number;
                }
            }
        }
        return ChartData;
    };


    stat_map.prototype.init_line = function () {

        var ChartData = this.get_stat_detail();
        this.lineChartData.labels = Object.keys(ChartData);
        this.lineChartData.datasets[0].data = Object.keys(ChartData).map(function (key) {
            return ChartData[key];
        });
        this.Line = new Chart(document.getElementById("canvas").getContext("2d")).Line(this.lineChartData, {
            pointHitDetectionRadius: 4,
            animationEasing: "easeInOutQuad"
        });
        // todo: set scale to max() for the regions
    };

    stat_map.prototype.update_line = function (ST_DV) {

        var ChartData = this.get_stat_detail(ST_DV);

        for (var i in this.Line.datasets[0].points) {
            var point = this.Line.datasets[0].points[i];
            var value = 0;
            if (ChartData[point.label]) {
                point.value = ChartData[point.label];
            }
        }

        this.Line.update();
    };


    stat_map.prototype.startUp = function (period) {

        if (this.loading) {
            return false;
        } else {
            this.loading = true;
        }

        this.period = period;
        var self = this;

        $.getJSON("/monitor/stat/" + period, function (data) {
                self.destroy();
                var MAX = 0;
                var result = [];

                for (var i = 0; i < data.length; i++) {
                    var item = data[i];
                    if (item.number > MAX) {
                        MAX = item.number;
                    }
                    result[item.ST_DV] = item.number;
                }

                self.grades = [0];
                var max_grades = Math.min(8, MAX);

                for (var i = 1; i <= max_grades; i++) {
                    self.grades[i] = Math.round(MAX * i / max_grades);
                }

                for (var i = 0; i < JSON1.features.length; i++) {
                    var feature = JSON1.features[i];
                    if (typeof result[feature.properties.ID_1] === 'undefined') {
                        feature.properties.number = 0;
                    } else {
                        feature.properties.number = result[feature.properties.ID_1];
                    }
                    feature.properties.color = self.getColor(feature.properties.number);
                }

                self.layer = L.geoJson(JSON1, {
                    style: function (feature) {
                        return {
                            fillColor: feature.properties.color,
                            weight: 0.5,
                            opacity: 1,
                            color: 'grey',
                            dashArray: '3',
                            fillOpacity: 0.6
                        };
                    },
                    onEachFeature: function (feature, layer) {
                        layer.on({
                            click: self.highlightFeature
                        });
                    }

                }).addTo(self.map);
                self.info.addTo(self.map);

                if (self.grades.length > 2) {
                    self.legend.addTo(self.map);
                }

                if (data.length) {

                    $.getJSON("/monitor/stat_detail/" + period, function (data) {
                        self.chart.addTo(self.map);
                        self.stat_detail = data;
                        self.init_line();
                        self.map.on('click', self.resetHighlight);

                        self.loading = false;
                        self.loaded = true;
                    });

                } else {

                    self.loading = false;
                    self.loaded = true;
                }

            }
        );
    };

    stat_map.prototype.destroy = function () {
        if (this.loaded) {
            this.layer.clearLayers();

            if (this.chart._map == this.map) {
                this.chart.removeFrom(this.map);
            }

            if (this.legend._map == this.map) {
                this.legend.removeFrom(this.map)
            }

            this.info.removeFrom(this.map);
            this.map.off('click', this.resetHighlight);
            this.loaded = false;
        }
    };

    return stat_map;
})();

var realtime_map = (function () {
    var realtime_map = function (map) {

        this.loaded = false;

        this.layer = [];
        this.markers = L.layerGroup();

        this.map = map;


        this.PERIOD_SECONDS = 15;
        this.PERIOD = this.PERIOD_SECONDS * 1000;
        this.marker_lifetime;

        this.MIN_OPACITY = 0.15;

        this.dots = {};
        this.step;
        this.max_age;

        this.dot_timer;
        this.JSON_timer;
        this.active_dot_id;

        this.PLAY_AUDIO = true;

        this.info = L.control({position: 'topright'});

        var self = this;

        this.volume_buttom = L.easyButton({
            states: [{
                stateName: 'sound',
                icon: 'fa-volume-up fa-lg',
                title: 'sound on',
                onClick: function (btn, map) {
                    self.PLAY_AUDIO = false;
                    btn.state('nosound');
                }
            }, {
                stateName: 'nosound',
                icon: 'fa-volume-off fa-lg',
                title: 'sound off',
                onClick: function (btn, map) {
                    self.PLAY_AUDIO = true;
                    btn.state('sound');
                }
            }]
        });

        this.info.onAdd = function (map) {

            this._div = L.DomUtil.create('div', 'info');
            $(this._div).html(self.INFO_MESSAGE);

            return this._div;
        };

        this.info_set = function (dot, last) {
            var message = "<h4>" + gettext(dot.layer.getLayers()[0].feature.properties.NAME_2) + "<h4/>" +

                (dot.NSEX == 1 ? '<i class="fa fa-male"></i>' : '<i class="fa fa-female"></i>') + " " +
                moment.duration(-dot.age, "seconds").humanize(true);// +
                //"<br/>" +
                //moment(dot.created_at).format("dddd, h:mm:ss a");

            if (last) {
                message = "<h3>" + gettext("Last registration:") + "</h3>"
                    + message +
                    "<p>" + gettext("Hover over a marker") + "</p>";
            }

            $(this.info.getContainer()).html(message);
        };

        this.highlightFeature = function (e) {
            var marker = e.target;
            var dot = self.dots[marker.options.dot_id];
            self.info_set(dot);
        };

        this.resetHighlight = function (e) {
            self.info_set(self.active_dot_id, true);
        };

        this.seed = 1;

        this.random = function () {
            var x = Math.sin(this.seed++) * 10000;
            return x - Math.floor(x);
        }

    };

    realtime_map.prototype._get_all_paths = function (layer, paths) {
        var self = this;
        if (layer._path) {
            paths.push(layer._path);
        } else {
            layer.eachLayer(function (layer) {
                    paths.concat(
                        self._get_all_paths(layer, paths)
                    );
                }
            )
        }
        return paths;
    };

    realtime_map.prototype.get_all_paths = function (layer) {
        return this._get_all_paths(layer, [])
    };

    realtime_map.prototype.get_layer_for_dot = function (dot) {
        var layer = false;
        this.layer.eachLayer(function (l) {
            if (l.feature.properties.ID_2 == dot.DIS) {
                layer = l;
            }
        });
        return layer;
    };

    realtime_map.prototype.process_data = function (data, max_age) {

        for (var id in this.dots) {
            this.dots[id].delete = true;
        }

        var new_dots = 0;
        var delayed_dots = 0;
        var old_dots = 0;

        for (var i in data) {
            var dot = data[i];

            // find dot in dots
            if (typeof this.dots[dot.id] === 'undefined') {
                new_dots++;

                // do not have this one yet
                dot.delay = (dot.age < this.PERIOD_SECONDS);
                if (dot.delay) {
                    delayed_dots++;
                }

                dot.plotted = false;
                dot.opacity = (1 - dot.age / max_age) * (1 - this.MIN_OPACITY) + this.MIN_OPACITY;

                if (DEBUG) {
                    console.log("new dot: " + dot.id + " age: " + dot.age + " max_age: " + max_age + " opacity: " + dot.opacity);
                }

                this.dots[dot.id] = dot;
            } else {
                this.dots[dot.id].delete = false;
                old_dots++;
            }
        }

        if (DEBUG) {
            console.group("Dots:");
            console.log("old" + old_dots);
            console.log("new" + new_dots);
            console.log("delayed" + delayed_dots);
            console.log("total" + Object.keys(this.dots).length);
            console.groupEnd();
        }

        delayed_dots = 0;

        for (var id in this.dots) {
            var dot = this.dots[id];

            if (!dot.plotted && !dot.delay) {
                this.plot_a_dot(id);
                this.active_dot_id = dot;
            }
            if (!dot.plotted && dot.delay) {
                delayed_dots++;
            }
        }

        if (delayed_dots) {
            this.step = this.PERIOD / (delayed_dots + 1);
            this.plot_delayed_dots(this);
        } else {
            this.info_set(this.active_dot_id, true);
            if (!this.active_dot_id.marker.isBouncing()) {
                L.Marker.stopAllBouncingMarkers();
                this.active_dot_id.marker.bounce();
            }

        }

        for (var id in this.dots) {
            var dot = this.dots[id];
            if (dot.delete) {
                this.delete_dot_properties(dot);
                delete dot;
            }
        }
    };

    realtime_map.prototype.plot_delayed_dots = function (self) {
        var found = false;
        for (var id in self.dots) {
            var dot = self.dots[id];
            if (!dot.plotted && dot.delay) {
                found = true;
                self.plot_a_dot(id);
                break;
            }
        }
        if (found) {
            (function (self) {
                self.dot_timer = setTimeout(self.plot_delayed_dots, self.step, self);
            })(self);
        }
    };

    realtime_map.prototype.plot_a_dot = function (id) {
        var dot = this.dots[id];

        if (dot.plotted) {
            return false;
        } else {
            dot.plotted = true;
        }

        var layer = this.get_layer_for_dot(dot);

        if (!layer) {

            console.group("layer was not found:");
            console.error(dot.DIS);
            console.dir(dot);
            console.groupEnd();

            return false;
        }

        dot.layer = L.geoJson(layer.feature, {
            style: {
                color: dot.NSEX == 2 ? 'pink' : 'lightblue',
                weight: 1,
                fillOpacity: dot.opacity / 2,
                opacity: 1
            }
        }).addTo(this.map);

        var icon = dot.NSEX == 2 ? L.AwesomeMarkers.icon({
            icon: 'female',
            prefix: 'fa',
            markerColor: 'lightred'
        }) : L.AwesomeMarkers.icon({
            icon: 'male',
            prefix: 'fa',
            markerColor: 'lightblue'
        });

        var center = layer.getBounds().getCenter();
        var baseJitter = 0.15;
        center.lat = center.lat - baseJitter / 2 + this.random() * baseJitter;
        center.lng = center.lng - baseJitter / 2 + this.random() * baseJitter;

        dot.marker = L.marker(
            center,
            {
                icon: icon,
                opacity: dot.opacity,
                dot_id: dot.id
            }
        ).addTo(this.map);
        this.oms.addMarker(dot.marker);

        dot.marker.on({
            mouseover: this.highlightFeature,
            mouseout: this.resetHighlight
        });

        if (dot.delay) {
            L.Marker.stopAllBouncingMarkers();
            dot.marker.bounce();
            this.info_set(dot, true);
            this.active_dot_id = dot;
            if (this.PLAY_AUDIO) {
                audioElement.play();
            }
        }

        var self = this;
        (function (id) {
            var dot = self.dots[id];
            $(self.get_all_paths(dot.layer)).animate(
                {opacity: self.MIN_OPACITY / 2},
                self.marker_lifetime
            );

            $([dot.marker._icon, dot.marker._shadow]).animate(
                {opacity: self.MIN_OPACITY},
                self.marker_lifetime,

                function () {
                    self.map.removeLayer(dot.marker);
                    self.map.removeLayer(dot.layer);

                    delete dot.marker;
                    delete dot.layer;
                }
            );
        })(id);
    };

    realtime_map.prototype.loadJSON = function (self) {
        $.getJSON("/monitor/realtime", function (data) {
            if (data.length) {
                self.step = self.PERIOD / data.length;

                self.max_age = 1;
                for (var i in data) {
                    var age = data[i].age;
                    if (age > self.max_age) {
                        self.max_age = age;
                    }
                }

                self.marker_lifetime = self.max_age * 1000;
                self.process_data(data, self.max_age);
            }
            self.loaded = true;

        });

        (function (self) {
            self.JSON_timer = setTimeout(self.loadJSON, self.PERIOD, self);
        })(self);
    };


    realtime_map.prototype.startUp = function () {
        this.layer = L.geoJson(JSON3, {
            style: {
                weight: 0,
                fillOpacity: 0
            }
        }).addTo(this.map);

        this.info.addTo(this.map);
        this.oms = new OverlappingMarkerSpiderfier(this.map);
        this.volume_buttom.addTo(this.map);

        this.loadJSON(this);
    };

    realtime_map.prototype.delete_dot_properties = function (dot) {
        if (dot.marker) {
            this.map.removeLayer(dot.marker);
        }
        if (dot.layer) {
            this.map.removeLayer(dot.layer);
        }
    };

    realtime_map.prototype.destroy = function () {
        if (this.loaded) {
            clearTimeout(this.dot_timer);
            clearTimeout(this.JSON_timer);

            for (var id in this.dots) {
                var dot = this.dots[id];
                this.delete_dot_properties(dot);
                delete dot;
            }
            this.dots = {};
            this.info.removeFrom(this.map);
            this.map.removeLayer(this.layer);
            this.volume_buttom.removeFrom(this.map);
            this.loaded = false;
        }
    };

    return realtime_map;
})();

