from collect_warrior.tools.base_tool import BaseTool


class SearchTool(BaseTool):

    def __init__(self):
        self.proxy = None
        self.timeout = None

    def get_name(self):
        return "search"

    def get_description(self):
        return "This tool is used to search on the Internet"

    def get_params(self):
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string"
                },
                "engine": {
                    "type": "string",
                    "default": "duckduckgo"
                },
                "limit": {},
                "offset": {},
            },
            "required": ["query"]
        }

    def execute(self, query, engine, lang, max_results, **kwargs):
        if engine != "duckduckgo":
            raise ValueError("Unsupported engine %s" % engine)

        return self.__search_ddgs_result(query, lang, max_results, **kwargs)

    def __search_ddgs_result(self, query, lang, max_results, **kwargs):
        from ddgs import DDGS
        region = self._get_region(lang)
        with DDGS(proxy=self.proxy, timeout=self.timeout) as ddgs:
            search_results = ddgs.text(query=query, safesearch="moderate", max_results=max_results, region=region, **kwargs)
        results = []
        for sr in search_results:
            results.append({
                "title": sr.get("title", ""),
                "body": sr.get("body", ""),
                "href": sr.get("href", ""),
                "source": "duckduckgo"
            })
        return results

    def _get_region(self, lang: str) -> str:
        """Get region code based on language (for DuckDuckGo)"""
        region_map = {
            "zh-cn": "cn-zh",
            "zh": "cn-zh",
            "en": "us-en",
            "en-us": "us-en",
            "en-gb": "gb-en",
            "ja": "jp-ja",
            "ko": "kr-ko",
            "fr": "fr-fr",
            "de": "de-de",
            "es": "es-es",
            "ru": "ru-ru",
        }

        return region_map.get(lang.lower(), "wt-wt")  # wt-wt means no specific region

