{
    'name' : 'Andara Low Stock Notify',
    'version' : '1.0',
    'author' : 'Bydev',
    'summary' : '',
    'description' : '',
    'category' : 'Sales Management',
    'depends' : ['base', 'mail', 'product'],
    'data':[
    			'data/email_template.xml',
                'views/product_template.xml',
                'views/ir_cron.xml'
    		],
    'installable': True
}
