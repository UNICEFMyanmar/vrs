window.CSRFMIDDLEWARETOKENNAME = "csrfmiddlewaretoken";

function form2string($form) {
    return JSON.stringify($form.serializeArray());
}

function string2form($form, serializedStr) {
    var fields = JSON.parse(serializedStr);
    for (var i = 0; i < fields.length; i++) {
        var controlName = fields[i].name;
        var controlValue = fields[i].value;

        if (controlName != CSRFMIDDLEWARETOKENNAME) {
            var el = $form.find("[name=" + controlName + "]");
            el.val(controlValue);
            if ( el.is( "select" ) ) {
                el.select2("val", controlValue);
            }
        }
    }
}

var FForm = Backbone.Model.extend({
        defaults: {
            serial: "---",
            date: moment(),
            user: "---",
            description: "---"
        },
        remove: function () {
            this.destroy();
        }
    }
);

window.FFormView = Backbone.View.extend({
    tagName: 'tr',

    initialize: function (options) {
        this.options = options;
    },

    events: {
        "click .glyphicon-cloud-upload": "load_click",
        "click .glyphicon-remove": "delete_click"
    },

    delete_click: function (event) {
        this.remove();
        this.model.destroy();
    },
    load_click: function (event) {
        string2form($("#" + window.FORM_ID), this.model.attributes.form);
        $("a[href='#home']").click();
        this.model.destroy();
    },

    template: _.template($('#item-template').html()),

    render: function () {
        $(this.el).html(
            this.template(
                this.model.toJSON()
            )
        );
        return this;
    }
});

window.FFormCollection = Backbone.Collection.extend(
    {
        model: FForm,
        localStorage: new Backbone.LocalStorage(window.FORM_ID),
        //comparator: function (obj1, obj2) {
        //    return obj1.get('number').localeCompare(obj2.get('number'));
        //}
    }
);

window.FFormListView = Backbone.View.extend({
    el: $("tbody"),

    initialize: function (options) {
        this.options = options;
        this.fforms = new FFormCollection();
        this.fforms.bind('all', this.render, this);
        this.fforms.fetch();
        //this.fforms.fetch(this.ajax_options);
    },

    addOne: function (fform) {
        this.$el.append(
            new FFormView(
                {
                    model: fform,
                    app: this.options.app,
                    el: $(document.createElement('tr'))
                }
            ).render().el);
        return this;
    },

    addNew: function (fform) {
        return this.fforms.create(fform);
    },

    render: function () {
        this.$el.empty();
        this.fforms.each(this.addOne, this);
        var count = "";
        if (this.fforms.length) {
            count = this.fforms.length;
        }
        $('.badge').html(count);
        return this;
    }
});

window.AppView = Backbone.View.extend({
    el: 'body',
    initialize: function () {
        this.FFormList = new FFormListView({app: this});
        this.form = $("#" + window.FORM_ID)
    },

    events: {
        "click #save_form_button": "addFForm"
    },

    render: function () {
        this.$el.find('table').append(this.FFormList.render().el);
    },

    addFForm: function () {
        var id = $("#" + window.SERIAL_ID)[0].value;
        var a =  this.form.serializeArray();
        var description = "";
        for (key in a){
            var name = a[key].name;
            var value = a[key].value;
            if ((value)&&(name!=CSRFMIDDLEWARETOKENNAME)) {
                description += name+":"+value+",";
            }
        }
        this.FFormList.addNew(
            new FForm(
                {
                    serial: id,
                    date: moment(),
                    user: window.DJANGO_USER,
                    form: form2string(this.form),
                    description: description.substring(0, 40)
                }
            )
        );
        this.form.trigger("reset");
        this.form.find("select").select2("val", "");
        this.render()
    }
});

$(function () {
    window.app = new AppView();

    setInterval(function () {
        app.render();
    }, 10 * 1000);

});