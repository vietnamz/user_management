package apigateway.filter;

import apigateway.config.ApplicationProperties;
import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;
import org.springframework.beans.factory.annotation.Autowired;

import javax.servlet.http.HttpServletRequest;


public class PreFilter extends ZuulFilter {

    @Autowired
    private ApplicationProperties properties;

    @Override
    public String filterType() {
        return "pre";
    }

    @Override
    public int filterOrder() {
        return 1;
    }

    @Override
    public boolean shouldFilter() {
        return true;
    }

    @Override
    public Object run() {
        RequestContext ctx = RequestContext.getCurrentContext();
        HttpServletRequest request = ctx.getRequest();
        String accessToken = properties.getDefaultAccessToken();
        String authType = properties.getAuthenticationType();
        String requestHeader = request.getHeader(authType);
        /*if (!accessToken.equals(requestHeader)) {
            ctx.setResponseStatusCode(400);
            ctx.setResponseBody("access denied");
            ctx.setSendZuulResponse(false);
        }*/
        return null;
    }
}
