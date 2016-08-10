$(function () {
    function setup_location_triple_logic(id_ST_DV, id_DIS, id_TWN) {
        $(id_ST_DV).on('change', function (e) {
            var that = this;
            setTimeout(function () {
                enable_group(that, id_DIS);
            }, 1);
        }).trigger("change");

        $(id_DIS).on('change', function (e) {
            var that = this;
            setTimeout(function () {
                enable_group(that, id_TWN);
            }, 1);
        }).trigger("change");
    }

    function setup_location_logic(id_ST_DV, id_DIS, id_TWN, id_NR_AREA, id_CIR, id_RHC) {

        setup_location_triple_logic(id_ST_DV, id_DIS, id_TWN);

        $(id_TWN).on('change', function (e) {
            var that = this;

            setTimeout(function () {
                enable_group(that, id_RHC);
            }, 1);

            setTimeout(function () {
                var el = $('#id_Hospital');

                el.highlight_and_off();

                var opt_group = 'optgroup[label="' + $(that).select2('data').text + '"]';

                if (el.find(opt_group).length) {
                    el.find(opt_group + ', ' + opt_group + ' option').removeAttr('disabled').removeClass('hidden');
                } else {
                    el.find('optgroup').attr('disabled', 'disabled').addClass('hidden');
                }

            }, 1);

            var sub_code_no_el = $(id_CIR);

            sub_code_no_el.highlight_and_off();

            var opt_group = 'optgroup[label="' + $(this).select2('data').text + '"]';

            if (sub_code_no_el.find(opt_group).length) {
                sub_code_no_el.find('optgroup, option').attr('disabled', 'disabled').addClass('hidden');
                sub_code_no_el.find(opt_group + ', ' + opt_group + ' option').removeAttr('disabled').removeClass('hidden');
            } else {
                if ($(id_ST_DV).select2("val") != YANGON_STATE_DIVISION_CODE) {
                    sub_code_no_el.find('optgroup, option').attr('disabled', 'disabled').addClass('hidden');
                    sub_code_no_el.find('option[value=' + ANY_HOSPITAL_CODE + ']').removeAttr('disabled').removeClass('hidden');
                    sub_code_no_el.find('option[value=""]').removeAttr('disabled').removeClass('hidden');

                } else {
                    sub_code_no_el.find('optgroup, option').attr('disabled', 'disabled').addClass('hidden');
                    sub_code_no_el.find('option[value=' + YANGON_HOSPITAL_NOT_MENTIONED_CODE + ']').removeAttr('disabled').removeClass('hidden');
                    sub_code_no_el.find('option[value=""]').removeAttr('disabled').removeClass('hidden');
                    sub_code_no_el.select2('val', YANGON_HOSPITAL_NOT_MENTIONED_CODE);
                }
            }

        }).trigger("change");

        $(id_NR_AREA).on('change', function (e) {

            if ($(this).val() == 2) {
                enable_select2(id_RHC);
            } else {
                disable_select2(id_RHC);
            }
        }).trigger("change");

        var hospital = "#id_Hospital";
        var gov = "#id_governmental_hospital";
        var prv = "#id_private_hospital";


        $(hospital).on('change', function (e) {
            if ($(this).val()) {
                $(gov).val("").attr('disabled', 'disabled');
                $(prv).val("").attr('disabled', 'disabled');
            } else {
                $(gov).removeAttr('disabled');
                $(prv).removeAttr('disabled');
            }
        });

        if ($(hospital).val()) {
            $(hospital).trigger('change')
        }

        $(prv).on('change', function (e) {
            if ($(this).val()) {
                disable_select2("#id_Hospital");
                $(gov).val("").attr('disabled', 'disabled');
            } else {
                enable_select2("#id_Hospital");
                $(gov).removeAttr('disabled');
            }
        });

        if ($(prv).val()) {
            $(prv).trigger('change')
        }


        $(gov).on('change', function (e) {
            if ($(this).val()) {
                disable_select2("#id_Hospital");
                $(prv).val("").attr('disabled', 'disabled');
            } else {
                enable_select2("#id_Hospital");
                $(prv).removeAttr('disabled');
            }
        });

        if ($(gov).val()) {
            $(gov).trigger('change')
        }

    }

    var NAGP_M = [];

    function setup_NAGP_M(selector) {
        $(selector).select2("enable", false);
        $(selector + " option").each(function () {
            var val = $(this).text().match(/\d+\.?\d*/g);
            if (val) NAGP_M.push(val);
        });
    }

    function set_NAGP_M(selector, value) {
        $(selector).highlight_and_off();

        var option = -1;
        if (value == NAGP_M[NAGP_M.length - 1][1]) { // last option is for unknown
            option = NAGP_M[NAGP_M.length - 1][0]
        } else if (value < NAGP_M[0][1]) { // lower then minimum
            option = NAGP_M[0][0]
        } else if (value >= NAGP_M[NAGP_M.length - 2][1]) { // higher then maximum
            option = NAGP_M[NAGP_M.length - 2][0]
        }
        else {
            for (i = 1; i < NAGP_M.length - 2; i++) { // exact value
                if ((value >= NAGP_M[i][1]) && (value <= NAGP_M[i][2])) {
                    option = NAGP_M[i][0];
                    break;
                }
            }
        }
        if (option >= 0) $(selector).val(parseInt(option)).trigger("change");
    }

    function validate_date(value) {
        if (value.length != 8) {
            return false;
        } else {
            var dateArray = /(\d{2})(\d{2})(\d{4})/.exec(value);
            return !isNaN(
                    Date.parse(
                            dateArray[3] + '-' + dateArray[2] + '-' + dateArray[1]));
        }
    }

    function setup_validator() {
        $.validator.setDefaults({
            highlight: function (element) {
                $(element).closest('.form-group').addClass('has-error');
            },
            unhighlight: function (element) {
                $(element).closest('.form-group').removeClass('has-error');
            },
            errorElement: 'span',
            errorClass: 'help-block',
            errorPlacement: function (error, element) {
                if (element.parent('.input-group').length) {
                    error.insertAfter(element.parent());
                } else {
                    error.insertAfter(element);
                }
            }
        });
        $.validator.methods.date = function (value, element) {
            return this.optional(element) || validate_date(value);
        };

        $.validator.methods.age = function (value, element) {
            if (isNaN(value)) {
                return false;
            } else {
                return (value >= 15 && value <= 50) || (value == 99);
            }
        };

        $.validator.methods.pre_deli = function (value, element) {

            var sex = $("#id_SEX").val();

            if (sex == SEX_MALE && value != PRE_DELI_NOT_RELEVANT) {
                return false;
            }

            if (sex == SEX_FEMALE && value == PRE_DELI_NOT_RELEVANT) {
                return false;
            }

            return true;
        };

        /**
         * @return {boolean}
         */
        $.validator.methods.NMULTI_B_validation = function (value, element) {
            var NTYPE_B = $("#id_NTYPE_B").val();
            var range = [0, 99];

            if (NTYPE_B == 2) {
                range = [1, 10];
            } else if (NTYPE_B == 3) {
                range = [11, 30];
            } else {
                return true;
            }

            return ((value <= range[1]) && (value >= range[0]));
        }
    }


    function enable_group(that, element) {
        var el = $(element);

        el.highlight_and_off();

        var opt_group = 'optgroup[label="' + $(that).select2('data').text + '"]';
        if (el.find(opt_group).length) {
            el.find('optgroup, option').attr('disabled', 'disabled').addClass('hidden');
            el.find(opt_group + ', ' + opt_group + ' option').removeAttr('disabled').removeClass('hidden');
        } else {
            el.find('optgroup, option').removeAttr('disabled').removeClass('hidden');
        }
    }

    // http://stackoverflow.com/a/6216001/1852611
    function checkIfInView(element) {
        var offset = element.offset().top - $(window).scrollTop();
        if (offset > window.innerHeight) {
            // Not in view so scroll to it
            $('html,body').animate({scrollTop: offset - 50}, 1000);
            return false;
        }
        return true;
    }

    function disable_select2(selector, val) {
        var el = $(selector);
        val = typeof val !== 'undefined' ? val : "";

        el.highlight_and_off();

        el.val(val).trigger("change");
        el.select2("enable", false);
    }

    function enable_select2(selector) {
        var el = $(selector);

        el.highlight_and_off();
        el.select2("enable", true);
    }

    var FORM_SETTINGS = {};

    FORM_SETTINGS = {
        'f101_form': {
            LOGIC: true,
            DISABLE_SUBMIT_BY_ENTER: true,
            VALIDATION: true,
            selectorsWithFrame: ["#id_Date_of_Registration", "#id_NSEX", "#id_Occupation_F", "#id_Informer", "#id_NB_ALIV"],
            setup_form_validation: function () {
                $("#f101_form").validate({
                    ignore: [],
                            rules: {
                                'WEIGHT': {range: [1361, 5000]},
                                'NAGE_M': {age: true},
                                'PERIOD': {range: [28, 42]},
                                'NPRV_CH': {range: [0, 15]},
                                'NB_ALIV': {range: [0, 15]},
                                'Date_of_Birth': {date: true},
                                'Date_of_Registration': {date: true},
                                'NMULTI_B': {NMULTI_B_validation: true}
                            },
                            messages: {
                                'WEIGHT': gettext('Usually 1361 - 5000'),
                                'NAGE_M': gettext('Usually 15 - 50'),
                                'PERIOD': gettext('Usually 28 - 42'),
                                'NPRV_CH': gettext('Usually 0 - 15'),
                                'NB_ALIV': gettext('Usually 0 - 15'),
                                'Date_of_Birth': gettext('Please enter date in format DDMMYYYY'),
                                'Date_of_Registration': gettext('Please enter date in format DDMMYYYY'),
                                'NMULTI_B': gettext('Please check the value, should be 1 to 10 for twins or 11 to 30 for triplets')

                            },
                            invalidHandler: function (form) {
                                $('#confirm-submit').modal('show');
                            }
                        }
                );
            },

            setup_form_logic: function () {

                setup_location_logic('#id_ST_DV', '#id_DIS', '#id_TWN', '#id_NR_AREA', '#id_CIR', '#id_RHC')
                setup_location_triple_logic('#id_RST_DV', '#id_RDIS', '#id_RTWN');

                setup_NAGP_M('#id_NAGP_M');

                $("#id_NAGE_M").on('change', function () {
                    set_NAGP_M('#id_NAGP_M', $(this).val());
                });

                $('#id_NTYPE_B').on('change', function (e) {

                    if ($(this).val() == 1) {
                        disable_select2('#id_NMULTI_B');
                    } else {
                        enable_select2('#id_NMULTI_B');
                    }

                }).trigger("change");

                $('#id_NBTH').on('change', function (e) {
                    if ($(this).val() == 2) {
                        $("#id_NBTH_comment").highlight_and_off();
                        $("#id_NBTH_comment").removeAttr("disabled");
                    }
                    else {
                        $("#id_NBTH_comment").highlight_and_off();
                        $("#id_NBTH_comment").attr("disabled", "disabled");
                        $("#id_NBTH_comment").val("");
                    }

                }).trigger("change");


            }
        },
        'f201_form': {

            LOGIC: true,
            DISABLE_SUBMIT_BY_ENTER: true,
            VALIDATION: true,

            selectorsWithFrame: ["#id_private_hospital", "#id_Informant_name", "#id_N_CODE", "#id_PLD"],

            setup_form_logic: function () {

                setup_location_logic('#id_NNRT', '#id_NNRT1', '#id_NNST', '#id_NNVD', '#id_CIR', '#id_RHC')
                setup_location_triple_logic('#id_UPRS', '#id_UPRS1', '#id_UPCR');

                $('#id_SEX').on('change', function (e) {
                    var deli = $("#id_DELI");
                    var pre = $("#id_PRE");

                    if ($('#id_SEX').val() == SEX_MALE) {
                        disable_select2(deli);
                        disable_select2(pre);

                    } else {
                        enable_select2(deli);
                        enable_select2(pre);
                    }
                }).trigger("change");
            },

            setup_form_validation: function () {


                $.mask.definitions['Z'] = '[A-Z]';
                $.mask.definitions['V'] = '[V-Z]';
                $("#id_E_CODE").mask("V99.99");
                $("#id_N_CODE").mask("Z99.99");


                $("#f201_form").validate({
                            ignore: '',
                            rules: {
                                'SNER': {range: [1, 99999]},
                                'Date_of_Death': {date: true},
                                'Date_of_Registration': {date: true},
                                'DELI': {pre_deli: true},
                                'PRE': {pre_deli: true}
                            },
                            messages: {
                                'SNER': gettext('Bounds are: 1 - 99999'),
                                'Date_of_Death': gettext('Please enter date in format DDMMYYYY'),
                                'Date_of_Registration': gettext('Please enter date in format DDMMYYYY'),
                                'DELI': gettext('Please check this field value or "SEX" field value above'),
                                'PRE': gettext('Please check this field value or "SEX" field value above')

                            },
                            invalidHandler: function (form) {
                                $('#confirm-submit').modal('show');
                            }
                        }
                );
            }
        }
    };

    $.fn.highlight_and_off = function () {
        var _class = 'bg-success';
        var el = this.closest('.form-group');

        el.addClass(_class);

        setTimeout(function () {
            el.removeClass(_class);
        }, 300);
    };

    $("select").on("select2-blur", function (e) {
        $(this).valid();
    });

    getRHCValues();

    function getRHCValues() {
        $.ajax({
            url: '/rhc.json',
            type: 'get',
            dataType: 'json',
            cache: true,
            success: RHCfilloptions,
            async: true
        });
    }

    function RHCfilloptions(data) {
        var $select = $("#id_RHC");
        var selected_value = $("#id_RHC").find("option:selected").val();

        $select.find("optgroup").remove();
        $select.find("option").remove();

        $.each(data, function (i, optgroups) {
            $.each(optgroups, function (groupName, options) {
                    var label = optgroups[0];
                    if (typeof options === 'string') {
                        //var $option = $("<option>", {
                        //    text: label,
                        //    value: options
                        //});
                        //$option.appendTo($select);

                    }
                    else {
                        var $optgroup = $("<optgroup>", {
                            label: label
                        });
                        $optgroup.appendTo($select);

                        $.each(options, function (j, option) {
                            var $option = $("<option>", {
                                text: option[1],
                                value: option[0]
                            });
                            $option.appendTo($optgroup);
                        });
                    }
                }
            );
        });
        $("#id_RHC").find("option[value='" + selected_value + "']").attr("selected", "selected");
    }


    var form = $("form")[1];

        var form_settings = FORM_SETTINGS[form.id];

        if (form_settings.LOGIC) {
            form_settings.setup_form_logic();
        }
        if (form_settings.VALIDATION) {
            setup_validator();
            form_settings.setup_form_validation();
        } else {
            $("form").attr('novalidate', 'novalidate');
        }

        if (form_settings.DISABLE_SUBMIT_BY_ENTER) {
            $(form).on("keyup keypress", function (e) {
                var code = e.keyCode || e.which;
                if ((code == 13) && (!$(':focus').is('button[type="submit"]'))) {
                    e.preventDefault();
                    return false;
                }
            });
        }

        $('#submit_button').on("click", function () {
            $(form)[0].submit();
        });

        $(form_settings.selectorsWithFrame).each(function (index, item) {
            $(".form-group").has(item).css("border-bottom", "1px solid #888").css("margin-bottom", "2em").css("padding-bottom", "2em");
        });

        if ($(".has-error").length) {
            checkIfInView($(".has-error").first());
        }
        else {
            //$("#id_ST_DV").select2('open');
        }
    });