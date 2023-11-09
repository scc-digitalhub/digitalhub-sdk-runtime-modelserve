package it.smartcommunitylabdhub.core.models.entities.function.specs;

import it.smartcommunitylabdhub.core.annotations.common.SpecType;
import it.smartcommunitylabdhub.core.components.infrastructure.factories.specs.SpecEntity;
import it.smartcommunitylabdhub.core.exceptions.CoreException;
import it.smartcommunitylabdhub.core.utils.ErrorList;
import lombok.Getter;
import lombok.Setter;
import org.springframework.http.HttpStatus;

@Getter
@Setter
@SpecType(kind = "nefertem", entity = SpecEntity.FUNCTION)
public class FunctionNefertemSpec extends FunctionBaseSpec<FunctionNefertemSpec> {
    @Override
    protected void configureSpec(FunctionNefertemSpec functionNefertemSpec) {
        super.configureSpec(functionNefertemSpec);
        throw new CoreException(
                ErrorList.METHOD_NOT_IMPLEMENTED.getValue(),
                ErrorList.METHOD_NOT_IMPLEMENTED.getReason(),
                HttpStatus.INTERNAL_SERVER_ERROR
        );
    }
}