package apigateway.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;

// TODO: Auto-generated Javadoc

/**
 * Properties specific to API Gateway .
 *
 * <p>
 * Properties are configured in the application.yml file. See
 * {@link io.github.jhipster.config.JHipsterProperties} for a good example.
 */

@ConfigurationProperties(prefix = "application", ignoreUnknownFields = true)
public class ApplicationProperties {

    /**
     * The default access token.
     */
    @Value("${application.access_token}")
    private String defaultAccessToken;

    /**
     * The default authentication header
     */
    @Value("${application.auth_type}")
    private String authenticationType;

    public ApplicationProperties() {

    }

    public String getDefaultAccessToken() {
        return defaultAccessToken;
    }

    public void setDefaultAccessToken(String defaultAccessToken) {
        this.defaultAccessToken = defaultAccessToken;
    }

    public void setAuthenticationType(String authenticationType) {
        this.authenticationType = authenticationType;
    }

    public String getAuthenticationType() {
        return authenticationType;
    }
}
