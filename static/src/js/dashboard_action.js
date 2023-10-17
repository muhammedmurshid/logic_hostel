odoo.define('logic_hostel.dashboard_action', function (require){
    "use strict";
    console.log('))))')
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');
    var _t = core._t;
    var CustomDashBoard = AbstractAction.extend({
        template: 'CustomDashBoard',
        events:{
                'click .logic_hostel':'hostel_form',
                'click .logic_base':'logic_base',


                // uncomment the below line to view records on clicking the card
                // 'click .o_model_count': '_onCardActionClicked',
            },
        init: function(parent, context) {
           this._super(parent, context);
           this.dashboards_templates = ['DashboardProject'];
           this.today_sale = [];
           },
           willStart: function() {
           var self = this;
           return $.when(ajax.loadLibs(this), this._super()).then(function() {
               return self.fetch_data();
           });
           },
           start: function() {
               var self = this;
               this.set("title", 'Dashboard');
               return this._super().then(function() {
                   self.render_dashboards();
               });
           },

           render_dashboards: function(){
           var self = this;
           _.each(this.dashboards_templates, function(template) {
                   self.$('.o_pj_dashboard').append(QWeb.render(template, {widget: self}));
               });
               },
           fetch_data: function() {
               var self = this;
               var def1 =  this._rpc({
                      model: 'hostel.form',
                      method: 'get_hostel_datas'
               }).then(function(result)
            {
             console.log(result);
                self.total_projects = result['total_hostel'],
                self.total_tasks = result['total_tasks'],
                self.hostel_name = result['hostel_name']
                self.total_students = result['total_students']
           });
               return $.when(def1);
           },
           hostel_form: function(ev){
                console.log('ii')
                var self = this;
                ev.stopPropagation();
                ev.preventDefault();
    //            var $action = $(ev.currentTarget);
                console.log('entered function hr payslip')

                var options = {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb,
                };

                this.do_action({
                    name: _t("Logic Hostels"),
                    type: 'ir.actions.act_window',
                    res_model: 'hostel.form',
                    view_mode: 'tree,form,calendar',
                    views: [[false, 'list'],[false, 'form']],
                    domain: [['status','=', 'active']],
                    target: 'current' //self on some of them
                }, {
                        on_reverse_breadcrumb: this.on_reverse_breadcrumb
                });
            },
            logic_base: function(ev){
                console.log('ii')
                var self = this;
                ev.stopPropagation();
                ev.preventDefault();
    //            var $action = $(ev.currentTarget);
                console.log('entered function hr payslip')

                var options = {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb,
                };

                this.do_action({
                    name: _t("Logic Hostels"),
                    type: 'ir.actions.act_window',
                    res_model: 'logic.students',
                    view_mode: 'tree,form,calendar',
                    views: [[false, 'list'],[false, 'form']],
//                    domain: [['status','=', 'active']],
                    target: 'current' //self on some of them
                }, {
                        on_reverse_breadcrumb: this.on_reverse_breadcrumb
                });
            },

    })
    core.action_registry.add('dashboard_action', CustomDashBoard);
return CustomDashBoard;
})
