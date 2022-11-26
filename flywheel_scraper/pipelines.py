# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FlywheelScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # convert list to str
        adapter["url"] = adapter["url"][-1]
        adapter["address"] = adapter["address"][-1].strip().replace(",", "")
        adapter["business_name"] = adapter["business_name"][-1].strip()
        adapter["website"] = adapter["website"][-1].strip().replace("//", "")
        adapter["country"] = adapter["country"][-1].strip()
        adapter["detail"] = adapter["detail"][-1].strip()

        # extract each social from list of social
        for each_social in adapter["social"]:
            if "facebook" in each_social:
                adapter["facebook"] = each_social
            elif "twitter" in each_social:
                adapter["twitter"] = each_social
            elif "instagram" in each_social:
                adapter["instagram"] = each_social
            elif "linkedin" in each_social:
                adapter["linkedin"] = each_social

        return item
