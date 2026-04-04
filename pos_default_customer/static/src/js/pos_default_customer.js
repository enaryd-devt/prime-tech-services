/** @odoo-module **/

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    setup() {
        super.setup(...arguments);

        const config = this.config;

        if (config.default_partner_id) {
            const partnerId = config.default_partner_id[0];
            const partner = this.db.get_partner_by_id(partnerId);

            if (partner) {
                this.get_order().set_partner(partner);
            }
        }
    },

    add_new_order() {
        super.add_new_order(...arguments);

        const config = this.config;
        if (config.default_partner_id) {
            const partnerId = config.default_partner_id[0];
            const partner = this.db.get_partner_by_id(partnerId);

            if (partner) {
                this.get_order().set_partner(partner);
            }
        }
    },
});
