odoo.define('logic_hostel.dashboard_action', function (require){
    "use strict";
    console.log('))))')
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');
    var CustomDashBoard = AbstractAction.extend({
    template: 'CustomDashBoard',
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
              self.total_hostel = result['total_hostel'],
              self.total_employees = result['total_employees']
           });
               return $.when(def1);
       },


    })
    core.action_registry.add('dashboard_action', CustomDashBoard);
    return CustomDashBoard;
})
